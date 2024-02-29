import os
from typing import List, Optional

import numpy as np
import pandas as pd

from test_utils.path import get_test_data_dir


def get_parsing_measurements_dir() -> str:
    test_data_dir = os.path.join(get_test_data_dir(), "parsing_measurements")

    if not os.path.exists(test_data_dir):
        os.mkdir(test_data_dir)
        generate_data_for_parsing_measurements(test_data_dir)

    return test_data_dir


def generate_data_for_parsing_measurements(parsing_measurements_dir: str):
    generate_data_essential_light_curve(parsing_measurements_dir)  # time, flux, flux_err
    generate_data_light_curve_with_cbvs(parsing_measurements_dir)
    # TODO PEST-TEST


def generate_data_essential_light_curve(parsing_measurements_dir: str):
    df = get_essential_light_curve()
    name = "TIC123456789.01_20200101_TELESCOPE-NAME-0_Rc_measurements"
    save_dir = os.path.join(parsing_measurements_dir, "light_curve_lite")
    os.makedirs(save_dir, exist_ok=True)
    save_different_versions(df, save_dir, name)


def generate_data_light_curve_with_cbvs(parsing_measurements_dir: str):
    df = get_light_curve_with_cbvs(cbv_names=["AIRMASS", "Sky/Pixel_T1"])
    name = "TIC123456789.01_20200101_TELESCOPE-NAME-0_Rc_measurements"
    save_dir = os.path.join(parsing_measurements_dir, "light_curve_with_cbvs")
    os.makedirs(save_dir, exist_ok=True)
    save_different_versions(df, save_dir, name)


def save_different_versions(df: pd.DataFrame, path: str, name: str):
    """
    Generate three different versions with different separators, suffix, index and column information.
    """
    df.to_csv(os.path.join(path, f"{name}_without_header.txt"), sep=" ", index=False, header=False)
    df.to_csv(os.path.join(path, f"{name}_with_header.csv"), index=False, header=True)
    df.to_csv(os.path.join(path, f"{name}_with_index.tbl"), sep="\t", index=True, header=True)


def get_light_curve_with_cbvs(cbv_names: Optional[List[str]] = None) -> pd.DataFrame:
    if cbv_names is None:
        cbv_names = ["AIRMASS", "Sky/Pixel_T1"]

    df = get_essential_light_curve(columns=["BJD_TDB", "rel_flux_T1_n", "rel_flux_err_T1_n"])

    for cbv_name in cbv_names:
        df[cbv_name] = 1 + np.random.default_rng(42).random(df.shape[0])

    return df


def get_essential_light_curve(
    columns: Optional[List[str]] = None,
    n_measurements: int = 4,
    texp: float = 0.5 / 24,
    mean_flux: float = 1.0,
) -> pd.DataFrame:
    def get_time():
        start_time = 2.45900e06
        end_time = start_time + n_measurements * texp
        return np.linspace(start_time, end_time, num=n_measurements)
    
    if columns is None:
        columns = ["time", "flux", "flux_err"]

    time = get_time()
    flux = mean_flux * np.ones(n_measurements) + np.random.default_rng(42).normal(0, 1e-3, n_measurements)
    flux_err = np.full(n_measurements, 1e-3)

    df = pd.DataFrame(np.array([time, flux, flux_err]).T, columns=columns)

    return df
