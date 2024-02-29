import logging
import os
from typing import Any, List, Literal, Tuple, Union

import numpy as np
import pandas as pd

from exofop.extract.synonym_map import EssentialLightcurveAttributes

logger = logging.getLogger("exofop.extract")


DEFAULT_ESSENTIAL_ATTRIBUTE_NAMES = EssentialLightcurveAttributes()


def load_exofop_measurement_files_as_dfs(
    observation_names: List[str],
    data_dir: str,
    infer_separator: bool = True,
    essential_attribute_names: EssentialLightcurveAttributes = DEFAULT_ESSENTIAL_ATTRIBUTE_NAMES,
):
    """
    Load ExoFOP measurement files as DataFrames.

    Parameters:
    ----------
    observation_names : List[str]
        A list of observation names to load data from.

    data_dir : str
        The directory where ExoFOP measurement files are stored.

    infer_separator : bool, optional
        Whether to infer the separator used in the data files (default is True).

    Returns:
    --------
    Dict[str, pd.DataFrame]
        A dictionary where keys are observation names, and values are DataFrames
           containing measurement data or a tuple of DataFrames if multiple tables are found.
    measurement_file_names : List[str]
        A list of measurement file names corresponding to the loaded data.
    """

    def log_df_columns(df, observation_name):
        logger.debug(
            f"Observation {observation_name:<10s} | Number of columns: {len(df.columns)}"
            # + ("\n" if len(df.columns) >= 20 else "")
        )
        if len(df.columns) < 20:
            logger.debug(f'Concretely: {", ".join(df.columns)}.\n')

    measurement_file_names = []
    df_dict = {}

    for observation_name in observation_names:
        # Load DataFrame
        df, found_measurement_file = load_exofop_measurements_files_from_direcetory(
            data_dir,
            observation_name,
            infer_separator=infer_separator,
            essential_attribute_names=essential_attribute_names,
        )

        if df is None:  # No Data was found
            continue

        # Collect
        measurement_file_names.append(found_measurement_file)
        df_dict[observation_name] = df

        # if isinstance(df, list):
        #     print(len(df))
        #     print(found_measurement_file)

        # Log
        if isinstance(df, pd.DataFrame):
            log_df_columns(df, observation_name)
        elif isinstance(df, list):
            for i, df_ in enumerate(df):
                log_df_columns(df_, f"{observation_name}_{i}")

    logger.debug(
        "Data loading completed."
        f"Found the following measurement files: {measurement_file_names}"
        f" in {data_dir} with the following keys: {df_dict.keys()}"
    )

    return df_dict, measurement_file_names


def load_exofop_measurements_files_from_direcetory(
    data_dir: str,
    observation_name: str,
    infer_separator: bool = True,
    essential_attribute_names: EssentialLightcurveAttributes = DEFAULT_ESSENTIAL_ATTRIBUTE_NAMES,
):
    """Load an exofop measurement file from the given directory.


    Parameters
    ----------
    data_dir : str
        Path of the directory where the file is located.
    observation_name : str
        The name of the file to load.
    infer_seperator : bool
        Whether to infer the separator used in the file; defaults to True.
    essential_attribute_names: EssentialLightcurveAttributes
        Name of the essential light curve attributes to be used if there are no column names
        in the measurement file. Default is ("time", "flux", "flux_err").

    Returns
    -------
    pd.DataFrame
        The loaded data as a pandas DataFrame.

    Notes
    -----

    As specified in the TFOP SG1 Observation Guidelines Revision 6.4, the following files should be
    provided for an observation:
    - File 1: AstroImageJ Photometry Measurement Table (.tbl, .csv, .txt, .xls).
    - File 2: AstroImageJ Plot Configuration File (.plotcfg).
    - File 3: AstroImageJ Photometry Aperture File (.apertures).
    - File 4: Light Curve Plots (.png).
    - File 5: Field Image with Apertures (.png).
    - File 6: Plate Solved Image (.fit, .fits).
    - File 7: Seeing Profile (.png).
    - File 8: Notes and Results Text File (.txt).
    - File 9: Delta Magnitude (Dmag) vs. RMS Plot (.png).
    - File 10: NEB Table (.txt).
    - File 11: .zip file of NEB Depth Plot files.
    - File 12: Zoomed-in FOV Image (.png).

    Files 1-5 are automatically generated during AstroImageJ analysis results saving. AstroImageJ
    can also create all other files except the note file (File 8), which can be created using a text
    editor.

    As this function is to load the Photomertry Measurement Table, it looks for files in the
    specified directory that end with '.csv', '.tbl', '.txt', or '.xls'. Subsequently, it tries
    to load them as DataFrames.

    In case of PEST data, where both normalized and unnormalized flux is provided in different
    files, the function will join the two DataFrames on the index.
    """
    if not isinstance(essential_attribute_names, EssentialLightcurveAttributes):
        raise ValueError(
            "`'essential_attribute_names' must be an instance of the class "
            "EssentialLightcurveAttributes, containing fields (time, flux, flux_err)."
        )

    # Define path
    folder_path = os.path.join(data_dir, observation_name)
    valid_file_extensions = (".csv", ".tbl", ".txt", ".xls")
    excluded_terms = ("notes", "comment", "neb-table", "neb_table", "neighbourhood")

    # Find valid candidates for measurement files
    candidate_files = [
        file_name
        for file_name in os.listdir(folder_path)
        if file_name.lower().endswith(valid_file_extensions)
        and not any(term in file_name.lower() for term in excluded_terms)
    ]
    df_list = []
    found_measurement_files = []
    if len(candidate_files) != 1:
        logger.debug(f"Observation {observation_name} has candidate files: {candidate_files}")

    if any(("pest" in item.lower() for item in candidate_files)):
        df, measurement_file_name = load_measurements_pest(
            folder_path, candidate_files, essential_attribute_names=essential_attribute_names
        )
        found_measurement_files.append(measurement_file_name)
    else:
        standard_measurement_file_extensions = (
            "measurements.xls",
            "measurements.txt",
            "measurements.csv",
            "measurements.tbl",
        )
        for candidate_name in candidate_files:
            file_path = os.path.join(folder_path, candidate_name)
            if file_path.lower().endswith(standard_measurement_file_extensions):
                df = load_measurements_xls_txt_csv_tbl(file_path, infer_separator=infer_separator)
                found_measurement_files.append(file_path.split("/")[-1])
                df_list.append(df)
                logger.debug(df)

    if not found_measurement_files:
        logger.warning(
            f"Measurement files of observation {observation_name} do not adhere"
            "to standard naming conventions. Try to load anyways."
        )
        for candidate_name in candidate_files:
            file_path = os.path.join(folder_path, candidate_name)
            df = try_load_measurement_file_of_unknown_format(file_path)
            if df is None or len(df) == 0:  # No data was extracted
                continue

            # Known other formats
            df_has_column_names = df.columns.dtype != np.int64

            if df_has_column_names:
                logger.info(f"Found DataFrame with columns {df.columns}.")
            else:
                try:
                    df = try_infer_column_names(
                        df, file_path, observation_name, essential_attribute_names
                    )
                except Exception as e:
                    logger.info(
                        f"Unable to extract any measurements from file candidate {candidate_name}."
                    )
                    logger.debug(e)
                    continue

            found_measurement_files.append(candidate_name)
            df_list.append(df)

    if len(found_measurement_files) == 0:
        logger.error(f"No measurement file found in observation {observation_name}")
        return None, ""

    # Assure uniqueness of measurement file
    if len(found_measurement_files) > 1:
        competing_files = ", ".join(found_measurement_files)
        logger.debug(
            f"Competing measurement files {competing_files}" ' in observation "{observation_name}"'
        )

        return df_list, found_measurement_files

    if len(candidate_files) != 1 and not any(("pest" in item.lower() for item in candidate_files)):
        logger.info(f"Of the candidate files {found_measurement_files[0]} was chosen.")

    return df, found_measurement_files[0]


def load_generic_measurement_file(
    file_path: str, infer_separator: bool = True, **kwargs: Any
) -> pd.DataFrame:
    def check_if_string_is_numeric(string):
        components = string.split(".")
        return all(item.isnumeric() for item in components)

    def determine_index_col(file_path: str, **kwargs: Any) -> Union[int, None]:
        """Determine the appropriate index column for loading a CSV file."""
        potential_index = pd.read_csv(file_path, nrows=1, index_col=0, **kwargs).index[0]
        return 0 if potential_index in (0, 1) else None

    def determine_if_column_names_are_present(
        file_path, index_col, **kwargs: Any
    ) -> Union[Literal["infer"], None]:
        """If majority of column_names are purely numeric, they are not column names"""
        potential_column_names = pd.read_csv(
            file_path, nrows=1, index_col=index_col, **kwargs
        ).columns
        # CHECK if numeric
        number_of_numeric_columns = sum(
            check_if_string_is_numeric(name) for name in potential_column_names
        )

        majority_is_numeric = number_of_numeric_columns > len(potential_column_names) / 2

        return None if majority_is_numeric else "infer"

    if infer_separator:
        kwargs["sep"] = kwargs.get("sep", None)
        kwargs["engine"] = "python"

    index_col = determine_index_col(file_path, **kwargs)  # returns 0 or None
    if "names" not in kwargs:
        header = determine_if_column_names_are_present(file_path, index_col=index_col, **kwargs)
    else:
        header = None
    df = pd.read_csv(file_path, index_col=index_col, header=header, **kwargs)

    return df


def load_measurements_xls_txt_csv_tbl(file_path: str, infer_separator: bool = True) -> pd.DataFrame:
    """
    Load measurement data from various file formats.

    Parameters
    ----------
    file_path : str
        Path to the file containing measurement data.
    infer_separator : bool, optional
        If True, Python tries to guess the separators of the files (default is False).
        Guessing generally makes the functions slower.

    Returns
    -------
    pd.DataFrame
        Loaded measurement data as a pandas DataFrame.

    """

    if infer_separator:
        df = load_generic_measurement_file(file_path=file_path, infer_separator=True)
    else:
        # Asssuming that all but .cbv files are tab separated
        sep = None if file_path.lower().endswith(".cvb") else "\t"
        df = load_generic_measurement_file(file_path=file_path, infer_separator=False, sep=sep)
    return df


def load_measurements_pest(
    path,
    candidates,
    sep=r"\s+",
    essential_attribute_names: EssentialLightcurveAttributes = DEFAULT_ESSENTIAL_ATTRIBUTE_NAMES,
):
    """_summary_

    Parameters
    ----------
    file_path : str
        path to files

    # TODO What exactly is the difference between these two files?
    """

    def find_unique_matching_item(candidates, search_string):
        """
        Find a single item in the list that matches the given search string.

        Parameters
        ----------
        candidates : list
            A list of items to search through.
        search_string : str
            The string to search for in the items.

        Returns
        -------
        str
            The matching item.

        Raises
        ------
        AssertionError
            If zero or multiple matching items are found.
        """
        matching_items = [item for item in candidates if search_string in item]
        assert len(matching_items) != 0, (
            f"No matching item found for '{search_string}'" "among candidates: {candidates}"
        )
        assert len(matching_items) == 1, (
            f"More than one matching item found for '{search_string}'"
            "among candidates: {candidates}"
        )
        return matching_items[0]

    path_detrend_data = os.path.join(
        path, find_unique_matching_item(candidates, "detrend-data.txt")
    )
    path_data_name = os.path.join(path, find_unique_matching_item(candidates, "_data.txt"))

    # Flux wise not quite identical to the above one, e.g. 0.9988 vs. 0.9990
    # df_n = pd.read_csv(path_data_name, sep='\s+', index_col=None,
    #                    names=essential_attribute_names)
    df_n = load_generic_measurement_file(path_data_name, names=essential_attribute_names)

    # Detrend df can be either
    # ['#BJD_TDB', 'mag', 'mag_err', 'var_imag', 'comp_imag', 'x_coord',
    #  'y_coord', 'dist_center', 'fwhm', 'airmass', 'sky']
    # or
    # ['#BJD_TDB', 'flux', 'flux_err', 'var_flux', 'comp_flux', 'x_coord',
    #  'y_coord', 'dist_center', 'fwhm', 'airmass', 'sky']
    detrend_df = load_generic_measurement_file(path_detrend_data, sep=sep)

    if np.any(["mag" in column for column in detrend_df.columns]):
        flux, flux_err = magnitude_to_flux(
            magnitude=detrend_df.loc[:, "mag"].to_numpy(),
            magnitude_error=detrend_df.loc[:, "mag_err"].to_numpy(),
        )
        detrend_df.loc[:, "rel_flux_mag"] = flux / np.median(flux)
        detrend_df.loc[:, "rel_flux_err_mag"] = flux_err / np.median(flux)

        flux, flux_err = magnitude_to_flux(
            magnitude=df_n.loc[:, "rel_flux_T1_n"].to_numpy(),
            magnitude_error=df_n.loc[:, "rel_flux_err_T1_n"].to_numpy(),
        )
        df_n.loc[:, "rel_flux_T1_n"] = flux / np.median(flux)
        df_n.loc[:, "rel_flux_err_T1_n"] = flux_err / np.median(flux)
    else:
        # To distinguish them from detrended ones
        detrend_df.rename(
            {"flux": "rel_flux_T1_raw", "flux_err": "rel_flux_err_T1_raw"},
            axis="columns",
            inplace=True,
        )

    # ['#BJD_TDB', 'flux', 'flux_err', 'var_flux', 'comp_flux', 'x_coord',
    df = pd.concat([df_n, detrend_df], axis=1)

    assert np.all(df["#BJD_TDB"] == df.BJD_TDB), "Time arrays are not the same"
    df.drop(["#BJD_TDB"], axis=1, inplace=True)

    # if plot:
    #     flux_name_raw = 'rel_flux_mag' if 'rel_flux_mag' in df.columns else 'rel_flux_T1_raw'
    #     plt.plot(df['BJD_TDB'], df[flux_name_raw], label='Raw', ls='', marker='.')
    #     plt.plot(df['BJD_TDB'], df['rel_flux_T1_n'], label='Detrended', ls='', marker='.')
    #     plt.legend()
    #     plt.show()

    return df, path_data_name.split("/")[-1]


def try_load_measurement_file_of_unknown_format(file_path: str) -> Union[pd.DataFrame, None]:
    try:
        df = load_generic_measurement_file(file_path=file_path, infer_separator=True)
    except Exception:
        df = None
        logger.info(
            f"Unable to extract any measurements from file candidate {file_path.split('/')[-1]}."
        )

    return df


def try_infer_column_names(
    df,
    file_path,
    observation_name,
    essential_attribute_names: EssentialLightcurveAttributes = DEFAULT_ESSENTIAL_ATTRIBUTE_NAMES,
):
    if df.shape[1] == 3:  # time, flux, flux_err - a classic amongst the sloppy
        df = df.rename(columns=dict(zip(df.columns, essential_attribute_names)))
        logger.info(
            f"Found file {file_path.split('/')[-1]} with three columns"
            " and no header. Assume these are time, flux, flux_err "
            + f" with values like {df.iloc[0].values}."
        )

        assert np.any(
            df[essential_attribute_names.flux] > df[essential_attribute_names.flux_err]
        ), "Identified flux values are smaller than there errors."
    else:
        raise ValueError(
            f"Found file {file_path.split('/')[-1]} in observation {observation_name}"
            " with no header. Convert this file manually to something containing"
            f" {essential_attribute_names}."
        )
    return df


def check_uniqueness_of_column_names(df_list, observation_names):
    for df, observation_name in zip(df_list, observation_names):
        if df.columns.duplicated().any():
            duplicated_columns = df.columns[df.columns.duplicated()]
            logger.warning(
                f'Duplicate columns found in observation "{observation_name}": '
                f'{", ".join(duplicated_columns)}'
            )


def magnitude_to_flux(
    magnitude: Union[float, np.ndarray], magnitude_error: Union[float, np.ndarray]
) -> Tuple[Union[float, np.ndarray], Union[float, np.ndarray]]:
    """
    Convert magnitudes to fluxes using the inverse relationship.

    Parameters
    ----------
    magnitude : float
        Magnitude value.
    magnitude_error : float
        Uncertainty in the magnitude value.

    Returns
    -------
    tuple
        A tuple containing:
        - flux : float
            Calculated flux corresponding to the given magnitude.
        - flux_error : float
            Uncertainty in the calculated flux.

    Make sure to provide magnitude and magnitude_error in the same unit system.
    """
    flux = 10 ** (-0.4 * magnitude)  # Note that -0.4 = -1/2.5
    flux_error = 0.4 * np.log(10) * flux * magnitude_error

    return flux, flux_error
