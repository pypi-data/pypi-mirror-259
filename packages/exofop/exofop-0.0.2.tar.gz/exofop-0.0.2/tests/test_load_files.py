import logging
import os

import pandas as pd
import pytest
from exofop.extract.load_exofop_measurements_file import load_generic_measurement_file
from test_utils.generate_test_measurement_files import generate_data_for_parsing_measurements
from test_utils.path import get_test_data_dir

logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="module")
def test_files_dir():
    test_data_dir = os.path.join(get_test_data_dir(), "parsing_measurements")

    # Generate test data if it does not exist
    if not os.path.exists(test_data_dir):
        os.mkdir(test_data_dir)
        generate_data_for_parsing_measurements(test_data_dir)

    return test_data_dir


@pytest.mark.parametrize("sub_dir", ["light_curve_lite", "light_curve_with_cbvs"])
def test_load_generic_measurement(test_files_dir, sub_dir):
    data_dir = os.path.join(test_files_dir, sub_dir)

    for file_name in os.listdir(data_dir):
        # if keyword in file_name:
        df = load_generic_measurement_file(
            file_path=os.path.join(data_dir, file_name),
            infer_separator=True,
        )
        assert isinstance(df, pd.DataFrame)
        assert df.size > 0
        print(df)



