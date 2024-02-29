import os

import pandas as pd
import pytest
from exofop.extract import LightCurveTableList, SynonymMapLc

from test_utils.generate_test_measurement_files import generate_data_for_parsing_measurements
from test_utils.path import get_test_data_dir


@pytest.fixture(scope="module")
def light_curve_table_list():
    test_data_dir = os.path.join(get_test_data_dir(), "parsing_measurements")

    # Generate test data if it does not exist
    if not os.path.exists(test_data_dir):
        os.mkdir(test_data_dir)
        generate_data_for_parsing_measurements(test_data_dir)

    lcts = LightCurveTableList.load_exofop_data(
        target_dir=test_data_dir,
    )

    return lcts


def test_load_exofop_data(light_curve_table_list):
    lcts = light_curve_table_list
    assert isinstance(lcts, LightCurveTableList)


def test_synonym_map_property(light_curve_table_list):
    lcts = light_curve_table_list
    assert isinstance(lcts.synonym_map, SynonymMapLc)


def test_complete_property(light_curve_table_list):
    lcts = light_curve_table_list
    lcts.standardise_column_names()
    assert len(lcts.complete) == len(lcts)
    assert len(lcts.incomplete) == 0


def test_incomplete_property(light_curve_table_list):
    lcts = light_curve_table_list
    lcts[0].remove_column(lcts[0].synonym_map.light_curve_attributes.time)
    lcts[0].is_complete = lcts[0].check_completeness()

    assert len(lcts.complete) == len(lcts) - 1
    assert len(lcts.incomplete) == 1


def test_info_df(light_curve_table_list):
    lcts = light_curve_table_list
    info_df = lcts.info_df
    assert isinstance(info_df, pd.DataFrame)
    assert info_df.shape[0] == len(lcts)


def test_names_property_empty(light_curve_table_list):
    assert isinstance(light_curve_table_list.names, list)
    assert len(light_curve_table_list.names) > 0
