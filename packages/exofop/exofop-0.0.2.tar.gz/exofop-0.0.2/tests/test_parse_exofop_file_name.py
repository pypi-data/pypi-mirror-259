import unittest
from unittest.mock import patch, MagicMock

import pandas as pd

from exofop.extract.parse_exofop_file_name import (
    parse_exofop_file_name,
    modify_observatory_name_if_filter_too_long,
    convert_exofop_file_name_components,
    parse_and_format_exofop_file_name,
    update_info_df_by_file_name_components,
)


class TestParseExofopFileName(unittest.TestCase):

    def test_parse_exofop_file_name_valid(self):
        file_name = "TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv"
        result = parse_exofop_file_name(file_name)
        expected = {
            "target": "TIC254113311",
            "pp": "01",
            "yyyymmdd": "20200805",
            "observatory": "ASTEP-ANTARCTICA",
            "filter": "Rc",
            "filetype": "compstar-lightcurves",
            "ext": "csv",
            "full_file_name": "TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv",
        }
        self.assertEqual(result, expected)

    def test_parse_exofop_file_name_invalid(self):
        invalid_file_name = "invalid_filename.csv"
        with self.assertRaises(ValueError):
            parse_exofop_file_name(invalid_file_name)

    @patch("exofop.extract.parse_exofop_file_name.logger")
    def test_parse_exofop_file_name_incomplete(self, mock_logger):
        incomplete_filename = "TIC446549905-01_20190916_Brierfield0.36m_measurements.tbl"
        mock_logger.warning = MagicMock()
        result = parse_exofop_file_name(incomplete_filename)
        expected = {
            "target": "TIC446549905",
            "pp": "01",
            "yyyymmdd": "20190916",
            "full_file_name": "TIC446549905-01_20190916_Brierfield0.36m_measurements.tbl",
            "observatory": "Brierfield0.36m",
            "filetype": "measurements",
            "ext": "tbl",
            "filter": "unknown",
        }

        self.assertEqual(result, expected)
        mock_logger.warning.assert_called_once()

    @patch("exofop.extract.parse_exofop_file_name.logger")
    def test_modify_observatory_name_with_warning(self, mock_logger):
        file_name_components = {
            "target": "TIC254113311",
            "pp": "01",
            "yyyymmdd": "20200822",
            "observatory": "El",
            "filter": "Sauce",
            "filetype": "Rc-filter_measurements",
            "ext": "xls",
            "full_file_name": "TIC254113311.01_20200822_El_Sauce_Rc-filter_measurements.xls",
        }
        max_filter_name_length = 3

        # Mock the logger.warning function
        mock_logger.warning = MagicMock()

        result = modify_observatory_name_if_filter_too_long(
            file_name_components, max_filter_name_length
        )
        expected = {
            "target": "TIC254113311",
            "pp": "01",
            "yyyymmdd": "20200822",
            "observatory": "El-Sauce",
            "filter": "Rc",
            "filetype": "measurements",
            "ext": "xls",
            "full_file_name": "TIC254113311.01_20200822_El_Sauce_Rc-filter_measurements.xls",
        }

        self.assertEqual(result, expected)
        mock_logger.warning.assert_called_once_with(
            "The filter name 'Sauce' obtained from parsing"
            " file name 'TIC254113311.01_20200822_El_Sauce_Rc-filter_measurements.xls'"
            " is longer than the threshold of 3 characters."
            " Reparsing is attempted."
        )

    def test_convert_exofop_file_name_components(self):
        file_name_components = {
            "target": "TIC254113311",
            "pp": "01",
            "yyyymmdd": "20200805",
            "observatory": "ASTEP-ANTARCTICA",
            "filter": "Rc",
            "filetype": "compstar-lightcurves",
            "ext": "csv",
        }
        result = convert_exofop_file_name_components(file_name_components)
        self.assertEqual(result["yyyymmdd"], "2020-08-05")
        self.assertEqual(result["pp"], 1)
        self.assertAlmostEqual(result["jd"], 2459066.5, delta=0.001)

    def test_update_info_df(self):
        file_name_components_dict = {
            "obs1": parse_and_format_exofop_file_name(
                "TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_measurements.csv"
            ),
            "obs2": parse_and_format_exofop_file_name(
                "TIC254113311.02_20200901_ASTEP-ANTARCTICA_Rc_measurements.csv"
            ),
        }

        # Create an initial DataFrame
        initial_df = pd.DataFrame(
            columns=[
                "Date",
                "BJD",
                "Observatory",
                "Filter",
                "target",
                "pp",
                "Measurement file name",
                "full_file_name",
            ]
        )

        # Call the function to update the DataFrame
        updated_df = update_info_df_by_file_name_components(
            file_name_components_dict=file_name_components_dict, info_df=initial_df
        )

        # Check if the DataFrame has been updated correctly
        self.assertEqual(updated_df.loc["obs1", "Date"], "2020-08-05")
        self.assertEqual(updated_df.loc["obs2", "Filter"], "Rc")
        self.assertEqual(updated_df.loc["obs1", "pp"], 1)
        self.assertEqual(updated_df.loc["obs2", "Observatory"], "ASTEP-ANTARCTICA")
        self.assertEqual(updated_df.loc["obs1", "Measurement file name"], "measurements.csv")
        self.assertEqual(
            updated_df.loc["obs2", "full_file_name"],
            "TIC254113311.02_20200901_ASTEP-ANTARCTICA_Rc_measurements.csv",
        )


if __name__ == "__main__":
    unittest.main()
