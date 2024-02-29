import os
import pytest
import pandas as pd
from typing import Optional

from exofop.extract.extractor import (
    get_sorted_exofop_observation_list,
    LightCurveTableList,
    LightCurveTable,
    unpack_multiple_measurements_from_same_tag,
)
from exofop.extract.load_exofop_measurements_file import (
    load_exofop_measurement_files_as_dfs,
    load_exofop_measurements_files_from_direcetory,
)
from exofop.extract.parse_exofop_file_name import (
    extract_components_from_exofop_measurement_file_names,
)

from test_utils.generate_test_measurement_files import generate_data_for_parsing_measurements
from test_utils.path import get_test_data_dir


def number_of_files_in_dir(directory: str, exclude: Optional[list] = None) -> int:
    if exclude is None:
        exclude = []
    return len(
        [
            item
            for item in os.listdir(directory)
            if not item.startswith(".")
            and not any(excluded_item in item for excluded_item in exclude)
        ]
    )


@pytest.fixture(scope="module")
def test_files_dir():
    test_data_dir = os.path.join(get_test_data_dir(), "parsing_measurements")

    # Generate test data if it does not exist
    if not os.path.exists(test_data_dir):
        os.mkdir(test_data_dir)
        generate_data_for_parsing_measurements(test_data_dir)

    observation_names = get_sorted_exofop_observation_list(test_data_dir)

    return test_data_dir, observation_names


def test_load_exofop_measurements_files_from_direcetory(test_files_dir):
    test_data_dir, observation_names = test_files_dir

    for observation_name in observation_names:
        unformatted_df_list, _ = (
            load_exofop_measurements_files_from_direcetory(
                observation_name=observation_name,
                data_dir=test_data_dir,
                infer_separator=True,
                essential_attribute_names=LightCurveTable().synonym_map.light_curve_attributes,
            )
        )
        for item in unformatted_df_list:
            assert isinstance(item, pd.DataFrame)
            assert item.size > 0

        # Check if the number of files is the same as the number of dataframes
        exclude = ["without_header"] if observation_name == "light_curve_with_cbvs" else []
        number_of_files = number_of_files_in_dir(
            os.path.join(test_data_dir, observation_name), exclude=exclude
        )

        assert len(unformatted_df_list) == number_of_files


def test_load_exofop_measurement_files_as_dfs(test_files_dir):

    test_data_dir, observation_names = test_files_dir

    unformatted_df_dict, measurement_file_names = load_exofop_measurement_files_as_dfs(
        data_dir=test_data_dir,
        observation_names=observation_names,
        infer_separator=True,
        essential_attribute_names=LightCurveTable().synonym_map.light_curve_attributes,
    )

    assert len(measurement_file_names) == len(observation_names)
    for key, value in unformatted_df_dict.items():
        assert isinstance(value, list)
        assert len(value) > 0
        exclude = ["without_header"] if key == "light_curve_with_cbvs" else []
        number_of_files = number_of_files_in_dir(os.path.join(test_data_dir, key), exclude=exclude)
        assert len(value) == number_of_files
        for item in value:
            assert isinstance(item, pd.DataFrame)
            assert item.size > 0


def test_unpack_multiple_measurements_from_same_tag():
    measurement_file_names = [
        "TIC123456789.01_20200101_TELESCOPE-NAME-0_Rc_3px_measurements.csv",
        "TIC123456789.01_20200101_TELESCOPE-NAME-0_Rc_5px_measurements.tbl",
        "TIC123456789.01_20200101_TELESCOPE-NAME-0_Rc_10_px_measurements_without_header.txt"
    ]
    
    true_file_name_components_dict = extract_components_from_exofop_measurement_file_names(
            dict(zip(range(len(measurement_file_names)), range(len(measurement_file_names)))),
            measurement_file_names
        )
    
    nested_file_name_components_dict = {
        "0": list(true_file_name_components_dict.values()),
    }
    unformatted_df_dict = {"0": ["df_1", "df_2", "df_3"]}

    unpack_multiple_measurements_from_same_tag(nested_file_name_components_dict, unformatted_df_dict)

    assert list(unformatted_df_dict.keys()) == ['0_3px', '0_5px', '0_10_px_without_header']


def test_load_exofop_data(test_files_dir):
    test_data_dir, _ = test_files_dir
    lcts = LightCurveTableList.load_exofop_data(
        target_dir=test_data_dir,
    )
    for lct in lcts:
        assert isinstance(lct, LightCurveTable)
        assert len(lct) > 0
