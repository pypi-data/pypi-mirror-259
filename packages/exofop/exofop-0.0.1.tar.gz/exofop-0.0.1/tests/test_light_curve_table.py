import importlib.util

import numpy as np
import pytest
from exofop.extract import LightCurveTable
from numpy.testing import assert_array_equal


@pytest.fixture
def light_curve_table() -> LightCurveTable:
    data = [[1.0, 2, 3], [1.0, 0.9, 1.1], [0.05, 0.1, 0.075], [0.1, 0.1, 0.1], [0.2, 0.3, 0.4]]
    names = ["time", "flux", "flux_err", "sky", "airmass"]
    file_name = "TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv"
    return LightCurveTable(data, names=names, file_name=file_name)


@pytest.fixture
def light_curve_table_complete(light_curve_table) -> LightCurveTable:
    lc = light_curve_table
    lc.standardise_column_names()
    return lc


@pytest.fixture
def light_curve_table_incomplete(light_curve_table) -> LightCurveTable:
    lc = light_curve_table
    lc.remove_column("time")
    lc.standardise_column_names()
    return lc


def test_init(light_curve_table):
    lc = light_curve_table
    assert lc.colnames == ["time", "flux", "flux_err", "sky", "airmass"]


def test_standardise_column_names(light_curve_table):
    lc = light_curve_table.copy()
    lc.standardise_column_names()
    assert lc.colnames == [
        "BJD_TDB",
        "rel_flux_T1_n",
        "rel_flux_err_T1_n",
        "Sky/Pixel_T1",
        "AIRMASS",
    ]


def test_is_complete(light_curve_table):
    lc = light_curve_table.copy()
    is_complete = lc.check_completeness()
    assert is_complete is False

    lc.standardise_column_names()
    is_complete = lc.check_completeness()
    assert is_complete is True

    lc.remove_column(lc.synonym_map.light_curve_attributes.time)
    is_complete = lc.check_completeness()
    assert is_complete is False


@pytest.mark.parametrize("attribute", ["time", "flux", "flux_err"])
def test_attribute_exists(light_curve_table, attribute):
    lc = light_curve_table
    lc_std = lc.copy()
    lc_std.standardise_column_names()

    # Test getting the attribute
    assert_array_equal(getattr(lc_std, attribute).value, lc[attribute].value)

    # Test setting the attribute
    setattr(lc_std, attribute, 2)
    assert_array_equal(getattr(lc_std, attribute).value, np.full(len(lc), 2))


def test_attribute_nonexistent(light_curve_table):
    lc = light_curve_table
    lc.remove_column("time")
    lc.standardise_column_names()

    assert lc.time is None
    assert lc.flux is not None
    assert lc.flux_err is not None


def test_name(light_curve_table):
    lc = light_curve_table
    assert lc.name == "TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv"
    assert lc.meta["full_file_name"] == lc.name


def test_cbvs(light_curve_table_complete):
    lc = light_curve_table_complete

    cbvs = lc.cbvs()
    assert cbvs.colnames == ["AIRMASS", "Sky/Pixel_T1"]


def test_light_curve(light_curve_table):
    lc = light_curve_table
    with pytest.raises(ValueError):
        lc.light_curve()

    lc.standardise_column_names()
    lc_reduced = lc.light_curve()
    assert lc_reduced.colnames == list(lc.synonym_map.light_curve_attributes)


def test_apply_time_correction_in_case_of_discrepancy(light_curve_table):
    lc = light_curve_table
    lc.standardise_column_names()

    lc.apply_time_correction_in_case_of_discrepancy()
    assert lc.time.value[0] == lc.meta["jd"]


def test_apply_time_correction_in_case_of_discrepancy_no_discrepancy(light_curve_table_complete):
    lc = light_curve_table_complete
    lc.apply_time_correction_in_case_of_discrepancy()
    assert lc.time.value[0] == lc.meta["jd"]


def test_apply_time_correction_in_case_of_discrepancy_no_time(light_curve_table_complete):
    lc = light_curve_table_complete

    lc_copy = lc.copy()
    lc_copy.meta["jd"] = 0.0
    lc_copy.apply_time_correction_in_case_of_discrepancy()

    assert lc_copy.time.value[0] == lc.time.value[0]


def test_from_pandas(light_curve_table):
    lc = light_curve_table
    lc.standardise_column_names()
    df = lc.to_pandas()
    lc_from_pandas = LightCurveTable.from_pandas(df, file_name=lc.name)
    lc_from_pandas.check_completeness()

    assert lc_from_pandas.colnames == lc.colnames
    assert lc_from_pandas.meta == lc.meta
    assert np.all(lc_from_pandas == lc)


def test_parse_and_format_exofop_file_name(light_curve_table):
    lc = light_curve_table
    lc.standardise_column_names()
    parsed = lc.parse_and_format_exofop_file_name(lc.name)
    parsed["is_complete"] = lc.is_complete
    assert parsed == dict(lc.meta)


@pytest.mark.parametrize("method", ["plot", "scatter", "errorbar"])
def test_create_plot_method_plot(light_curve_table_complete, method):
    if importlib.util.find_spec("matplotlib") is not None:
        ax = light_curve_table_complete._create_plot(method=method)
        assert ax is not None
