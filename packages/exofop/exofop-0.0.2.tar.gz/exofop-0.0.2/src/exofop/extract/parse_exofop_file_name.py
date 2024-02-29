"""
ExoFOP File Processing Module

This module contains functions for parsing, formatting, and updating information from ExoFOP-style
file names. It provides utilities for extracting components such as target names, dates, observatories,
filters, and more, from filenames following the specified conventions.

Functions
---------
update_info_df_by_file_name_components(info_df=None, file_name_components_dict=None)
    Update or create a DataFrame with extracted components.

extract_components_from_exofop_measurement_file_names(observation_names, measurement_file_names)
    Extract components from measurement file names and organize in a dictionary.

parse_and_format_exofop_file_name(file_name, max_filter_name_length=3)
    Parse and format an ExoFOP-style file name.

parse_exofop_file_name(file_name)
    Parse an ExoFOP-style file name to extract relevant components.

modify_observatory_name_if_filter_too_long(file_name_components, max_filter_name_length=3)
    Check string length of filter name and resolve observatory name if necessary.

convert_exofop_file_name_components(file_name_components)
    Convert parsed components to desired formats.

"""

import logging
import re
from typing import Optional, Tuple, Union

import astropy.time
import numpy as np
import pandas as pd

logger = logging.getLogger("exofop.extract")


def update_info_df_by_file_name_components(
    file_name_components_dict: dict, info_df: Optional[pd.DataFrame] = None
) -> pd.DataFrame:
    """
    Update or create a DataFrame with extracted file name components.

    This function updates an existing DataFrame or creates a new one by populating it
    with extracted components from the 'file_name_components_dict'. The dictionary should
    contain observation names as keys and corresponding file name components as values.

    If 'info_df' is not provided, a new DataFrame will be created.

    Parameters
    ----------
    info_df : pandas.DataFrame or None, optional
        An existing DataFrame to be updated (default is None).
    file_name_components_dict : dict or None, optional
        A dictionary containing observation names and corresponding file name components.

    Returns
    -------
    pandas.DataFrame
        The updated or newly created DataFrame containing the extracted components.

    Examples
    --------
    >>> file_name_components_dict = {
    >>>     'obs1': parse_and_format_exofop_file_name(
                'TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_measurements.csv'),
    >>>     'obs2': parse_and_format_exofop_file_name(
                'TIC254113311.02_20200901_ASTEP-ANTARCTICA_Rc_measurements.csv'),
    >>> }
    >>> updated_df = update_info_df_by_file_name_components(
        file_name_components_dict=file_name_components_dict
    )
                Date      BJD       Observatory  ... pp Measurement file name    full_file_name
    obs1  2020-08-05  2459066  ASTEP-ANTARCTICA  ...  1      measurements.csv  TIC254113311....
    obs2  2020-09-01  2459093  ASTEP-ANTARCTICA  ...  2      measurements.csv  TIC254113311....

    """
    if info_df is None:
        info_df = pd.DataFrame(
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

    for index, entry in file_name_components_dict.items():
        info_df.loc[index, "Date"] = entry["yyyymmdd"]
        info_df.loc[index, "BJD"] = int(np.floor(entry["jd"]))
        info_df.loc[index, "Observatory"] = entry["observatory"]
        info_df.loc[index, "Filter"] = entry["filter"]
        info_df.loc[index, "target"] = entry["target"]
        info_df.loc[index, "pp"] = entry["pp"]
        info_df.loc[index, "Measurement file name"] = entry["filetype"] + "." + entry["ext"]
        info_df.loc[index, "full_file_name"] = entry["full_file_name"]

    info_df["BJD"] = info_df["BJD"].astype(int)
    info_df["pp"] = info_df["pp"].astype(int)

    return info_df


def parse_and_format_exofop_file_name(
    file_name: str, max_filter_name_length=3
) -> dict[str, Union[str, int, None]]:
    """
    Parse and format an ExoFOP-style file name to extract relevant components and convert them.

    This function takes an ExoFOP-style file name and performs the following steps:
    1. Parses the file name using the 'parse_exofop_file_name' function to extract its components.
    2. Modifies the observatory name if the filter name is too long using the
       'modify_observatory_name_if_filter_too_long' function.
    3. Converts certain components in the extracted data, such as 'yyyymmdd' to 'yyyy-mm-dd'
       and 'pp' to an integer, using the 'convert_exofop_file_name_components' function.

    Parameters
    ----------
    file_name : str
        The ExoFOP-style file name to be parsed and formatted.
    max_filter_name_length : int, optional
        Maximum allowed length of the filter name for modification (default is 3).

    Returns
    -------
    dict
        A dictionary containing the extracted and converted components of the file name:
        - 'target': TIC ID or EPIC ID including planet number
        - 'pp': Integer representation of the planet number
        - 'yyyymmdd': UT date/time of the beginning of the observation in 'yyyy-mm-dd' format
        - 'jd': Julian Date corresponding to the observation date
        - 'observatory': Name of the observatory
        - 'filter': Filter used
        - 'filetype': Abbreviated description of the file type
        - 'ext': Extension of the file

    Examples
    --------
    >>> file_name = 'TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv'
    >>> result = parse_and_format_exofop_file_name(file_name)
    >>> print(result)
    {
        'target': 'TIC254113311',
        'pp': 1,
        'yyyymmdd': '2020-08-05',
        'observatory': 'ASTEP-ANTARCTICA',
        'filter': 'Rc',
        'filetype': 'compstar-lightcurves',
        'ext': 'csv'
        'full_file_name': 'TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv',
        'jd': 2459066.5
    }

    """
    try:
        file_name_components = parse_exofop_file_name(file_name)

        modified_file_name_components = modify_observatory_name_if_filter_too_long(
            file_name_components, max_filter_name_length
        )
        converted_file_name_components = convert_exofop_file_name_components(
            modified_file_name_components
        )
    except Exception as e:
        logger.warning(f"Could not parse file name '{file_name}': {e}")
        converted_file_name_components = {
            "target": "unknown",
            "pp": "-1",
            "yyyymmdd": "1001-01-01",
            "observatory": "unknown",
            "filter": "xx",
            "filetype": "unknown",
            "full_file_name": file_name,
            "ext": "unknown",
            "jd": 0.0,
        }

    return converted_file_name_components


def parse_exofop_file_name(file_name: str) -> dict[str, str]:
    """
     Parse an ExoFOP-style file_name to extract relevant components.

     Parameters
     ----------
     file_name : str
         The file_name to be parsed. This should follow the naming convention specified in the
         TFOP SG1 Observation Guidelines Revision 6.4. The convention is as follows:
         "targetname-pp_yyyymmdd_observatory_filter_filetype.ext"
     Returns
     -------
     dict
         A dictionary containing the extracted components:
         - 'targetname_pp': TIC ID or EPIC ID including planet number
         - 'yyyymmdd': UT date/time of the beginning of the observation
         - 'observatory': Name of the observatory
         - 'filter': Filter used
         - 'filetype': Abbreviated description of the file type
         - 'ext': Extension of the file

     Note
     ----
     As specified in the TFOP SG1 Observation Guidelines Revision 6.4, the naming convention
     for files associated with an observation adheres to the following format:

     "targetname-pp_yyyymmdd_observatory_filter_filetype.ext"

     Each component of the file_name holds specific information:
     - 'targetname-pp': TIC ID or EPIC ID, including the planet number (pp).
     - 'yyyymmdd': UT date/time of the beginning of the observation.
     - 'observatory': Name of the observatory.
     - 'filter': Filter used.
     - 'filetype': Abbreviated description of the type of file.
     - 'ext': Appropriate extension for the type of file.

     Explanation of the pattern components
     - `(?P<name> ...)` defines a named capturing group that helps organize and access captured components.
     - `.+` captures one or more of any character except a new line.
     - `[-_.]` matches any one of the characters: hyphen, underscore, or period (some ExoFOP users are sloppy!).
     - `\d+` captures one or more digits.
     - `\d{8}` matches exactly 8 digits (representing year, month, and day).
     - `[a-zA-Z]+` matches one or more letters (case-insensitive).

     Examples
     --------
     >>> result = parse_exofop_file_name(
     >>>    file_name='TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv'
     >>> )
     >>> print(result)
    {
         'target': 'TIC254113311',
         'pp': '01',
         'yyyymmdd': '20200805',
         'observatory': 'ASTEP-ANTARCTICA',
         'filter': 'Rc',
         'filetype': 'compstar-lightcurves',
         'ext': 'csv'
     }

    In the case of an incomplete file name

    >>> result = parse_exofop_file_name(
    ...    file_name='TIC446549905-01_20190916_Brierfield0.36m_measurements.tbl'
    ... )
    """
    # Regular expression pattern to capture file_name components
    pattern = (
        r"(?P<target>.+)[-_.](?P<pp>\d+)_(?P<yyyymmdd>\d{8})_(?P<observatory>.+?)_"
        r"(?P<filter>[a-zA-Z]+)_(?P<filetype>.+)?\.(?P<ext>.+)"
    )

    prefix_pattern = r"(?P<target>.+)[-_.](?P<pp>\d+)_(?P<yyyymmdd>\d{8})"

    # Attempt to match the pattern in the file name
    if match := re.match(pattern, file_name):
        file_name_components = match.groupdict()
        file_name_components["full_file_name"] = file_name
        return file_name_components  # Return the extracted components as a dictionary
    elif match := re.match(prefix_pattern, file_name):  # Tries to match target, pp, yyyymmdd
        logger.warning(
            f"Invalid file name format: '{file_name}'." " Extracted components will be incomplete."
        )
        file_name_components = match.groupdict()
        file_name_components["full_file_name"] = file_name

        # Try extract other components from the remaining string
        rest_of_string = file_name[match.end() :].removeprefix("_")
        ignore_filter_pattern = r"(?P<observatory>.+?)_(?P<filetype>.+)?\.(?P<ext>.+)"

        if match := re.match(ignore_filter_pattern, rest_of_string):
            file_name_components.update(match.groupdict())
        else:
            file_name_components["observatory"] = "unknown"
            file_name_components["filetype"] = "unknown"
            file_name_components["ext"] = (
                "unknown" if "." not in rest_of_string else rest_of_string.split(".")[-1]
            )

        file_name_components["filter"] = "unknown"

        return file_name_components
    else:
        raise ValueError(f"Invalid file_name format: {file_name}")


def modify_observatory_name_if_filter_too_long(
    file_name_components: dict, max_filter_name_length: int = 3
) -> dict[str, str]:
    """
    Check filter length of file_name_components['filter_name'] and resolve observatory name if necessary.

    This function is designed to handle cases where an underscore is mistakenly used in the
    observatory name when a hyphen should have been used. It also assists in correctly extracting
    the filter and filetype components from the combined observatory_filter_filetype component
    of the file name.

    Parameters
    ----------
    file_name_components : dict
        Dictionary containing parsed components of an ExoFOP-style file name.
    max_filter_name_length : int, optional
        Maximum allowed length of filter name (default is 3).

    Returns
    -------
    file_name_components : dict
        Updated file_name_components dictionary.

    Examples
    --------
    >>> file_name = 'TIC254113311-01_20200822_El_Sauce_Rc-filter_measurements.xls'
    >>> file_name_components = parse_exofop_file_name(file_name)
    {'target': 'TIC254113311', 'pp': '01', 'yyyymmdd': '20200822', 'observatory': 'El',
     'filter': 'Sauce', 'filetype': 'Rc-filter_measurements', 'ext': 'xls'}
    >>> modify_observatory_name_if_filter_too_long(file_name_components, max_filter_name_length=3)
    {'target': 'TIC254113311', 'pp': '01', 'yyyymmdd': '20200822', 'observatory':
     'El-Sauce', 'filter': 'Rc', 'filetype': 'measurements', 'ext': 'xls'}

    """

    def underscore_in_observatory_name(
        observatory: str,
        filter_name: str,
        observatory_filter_filetype: str,
        max_filter_name_length: int = 3,
    ) -> Tuple[str, str, str]:
        """
        Resolve filter and filetype components for an ExoFOP-style file name.

        Parameters
        ----------
        observatory : str
            The observatory component of the file name.
        filter_name : str
            The filter name component of the file name.
        observatory_filter_filetype : str
            The combined observatory and filter filetype component of the file name.
        max_filter_name_length : int, optional
            Maximum allowed length of filter name (default is 3).

        Returns
        -------
        observatory : str
            Updated observatory name.
        filter_name : str
            Updated filter name.
        filetype : str
            Updated filetype name.

        """
        # If someone used an underscore in the observatory name when they should have used a hyphen
        observatory = observatory + "-" + filter_name

        # Extract filter and filetype
        filter_filetype = re.split(r"[-_]", observatory_filter_filetype)

        # Find the index of a valid filter name
        filter_ind = next(
            (i for i, item in enumerate(filter_filetype) if len(item) <= max_filter_name_length),
            None,
        )

        # If no valid filter name was found, return unchanged data
        if filter_ind is None:
            return observatory, filter_name, observatory_filter_filetype

        # Resolve filter and filetype
        observatory += "-".join(filter_filetype[:filter_ind]) if filter_ind > 0 else ""
        filter_name = filter_filetype[filter_ind]
        filetype = "_".join(
            [item for item in filter_filetype[filter_ind + 1 :] if "filter" not in item]
        )

        return observatory, filter_name, filetype

    if (
        len(file_name_components["filter"]) <= max_filter_name_length
        or file_name_components["filter"] == "unknown"
    ):
        return file_name_components

    logger.warning(
        f"The filter name '{file_name_components['filter']}' obtained from parsing"
        f" file name '{file_name_components['full_file_name']}'"
        f" is longer than the threshold of {max_filter_name_length} characters."
        " Reparsing is attempted."
    )

    updated_observatory, updated_filter, updated_filetype = underscore_in_observatory_name(
        file_name_components["observatory"],
        file_name_components["filter"],
        file_name_components["filetype"],
        max_filter_name_length,
    )

    file_name_components["observatory"] = updated_observatory
    file_name_components["filter"] = updated_filter
    file_name_components["filetype"] = updated_filetype

    return file_name_components


def extract_components_from_exofop_measurement_file_names(
    observation_names, measurement_file_names
):
    file_name_components_dict = {}

    for obs_ind, observation_name in enumerate(observation_names):
        if isinstance(measurement_file_names[obs_ind], str):
            file_name_components = parse_and_format_exofop_file_name(
                measurement_file_names[obs_ind]
            )

            # Collect
            file_name_components_dict[observation_name] = file_name_components
        elif isinstance(measurement_file_names[obs_ind], list):
            file_name_components_dict[observation_name] = []
            for file_name in measurement_file_names[obs_ind]:
                file_name_components = parse_and_format_exofop_file_name(file_name)
                file_name_components_dict[observation_name].append(file_name_components)

    return file_name_components_dict


def convert_exofop_file_name_components(
    file_name_components: dict,
) -> dict[str, Union[str, int, None]]:
    """
    Convert the extracted file_name_components from parse_exofop_file_name to desired formats.

    Specifically:
    1. Convert 'yyyymmdd' to 'yyyy-mm-dd' format
    2. 'pp' to integer numbers, e.g. '01' to 1
    3. Add Julian Date

    Parameters
    ----------
    file_name_components : dict
        Dictionary containing parsed components of an ExoFOP-style file name.

    Returns
    -------
    dict
        A dictionary with yyyymmdd converted to 'yyyy-mm-dd' format and pp converted to integer.

    Examples
    --------
    >>> result = parse_exofop_file_name(
    >>>    file_name='TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv'
    >>> )
    >>> convert_exofop_file_name_components(result)

    """

    def reformat_date(file_name_components):
        """Convert 'yyyymmdd' to 'yyyy-mm-dd' format"""
        if yyyymmdd := file_name_components.get("yyyymmdd"):
            formatted_date = f"{yyyymmdd[:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:8]}"
            return formatted_date

        return None

    def convert_pp_to_int(file_name_components):
        if pp := file_name_components.get("pp"):
            # Convert pp to an integer and return
            pp_value = int(pp)
            return pp_value

        return None

    converted_file_name_components = file_name_components.copy()

    # Convert 'yyyymmdd' to 'yyyy-mm-dd' format
    converted_file_name_components["yyyymmdd"] = reformat_date(file_name_components)

    converted_file_name_components["pp"] = convert_pp_to_int(file_name_components)

    # Add Julian Day (jd)
    converted_file_name_components["jd"] = astropy.time.Time(
        converted_file_name_components.get("yyyymmdd"), format="iso"
    ).jd

    return converted_file_name_components
