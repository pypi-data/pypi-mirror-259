__all__ = ["LightCurveTableList", "LightCurveTable"]

import logging
import os
import re
from typing import List, Optional, Union

import astropy.table
import numpy as np
import pandas as pd

from exofop.extract.load_exofop_measurements_file import (
    load_exofop_measurement_files_as_dfs,
)
from exofop.extract.parse_exofop_file_name import (
    extract_components_from_exofop_measurement_file_names,
    parse_and_format_exofop_file_name,
)
from exofop.extract.synonym_map import SynonymMap, SynonymMapLc
from exofop.utils.paths import MPLSTYLE

logger = logging.getLogger("exofop.extract")

SYNONYM_MAP = SynonymMapLc.load_from_config()

SYNONYM_MAP_LC = SYNONYM_MAP.deepcopy()
for item in SYNONYM_MAP_LC.cbv_names:
    del SYNONYM_MAP_LC[item]


class LightCurveTable(astropy.table.Table):
    """
    A custom table class for representing light curve data.

    This class extends the functionality of `astropy.table.Table` and includes
    an additional attribute 'complete' to store information about the
    completeness of the light curve data.

    Parameters
    ----------
    data : array-like, dict, or Table, optional
        The data to be stored in the table. This can be an array-like object, a dictionary,
        or another Table. If not provided, an empty table will be created.
    name : str, optional
        The name of the observation.
    file_name : str, optional
        The measurement filename of the observation.
    meta : dict, optional
        A dictionary containing meta data for the table.
    args, kwargs

    Examples
    --------
    >>> from exofop.extract import LightCurveTable
    >>> lc = LightCurveTable(
    ...     [[1., 2, 3], [1., 0.9, 1.1], [0.05, 0.1, 0.075], [0.1, 0.1, 0.1], [0.2, 0.3, 0.4]],
    ...     names=["time", "flux", "flux_err", "sky", "airmass"],
    ...     file_name='TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv'
    ... )
    <LightCurveTable length=3>
    time    flux  flux_err   sky   airmass
    float64 float64 float64  float64 float64
    ------- ------- -------- ------- -------
        1.0     1.0     0.05     0.1     0.2
        2.0     0.9      0.1     0.1     0.3
        3.0     1.1    0.075     0.1     0.4

    We can standardise the column names using the synonym map:

    >>> lc.standardise_column_names()
    >>> lc.is_complete
    True

    After standardisation, we can access time, flux, and flux_err columns as attributes:

    >>> lc.time.value
    array([1., 2., 3.])
    >>> lc.flux.value
    array([1. , 0.9, 1.1])

    We can also apply a time correction if there is a discrepancy between the time in the file name
    and the time array:

    >>> lc.apply_time_correction_in_case_of_discrepancy()

    We can get the cotrending basis vectors (CBVs), i.e. all primary aliases of
    lc.synonym_map that do not represent time, flux or flux_err:

    >>> lc.cbvs()
    <LightCurveTable length=3>
    AIRMASS Sky/Pixel_T1
    float64   float64
    ------- ------------
        0.2          0.1
        0.3          0.1
        0.4          0.1

    """

    # synonym_map_lc = SYNONYM_MAP_LC
    simple_synonym_map: SynonymMapLc = SYNONYM_MAP_LC
    _synonym_map: SynonymMapLc = SYNONYM_MAP
    time_threshold: float = 3

    def __init__(
        self,
        *args,
        name: Optional[str] = None,
        file_name: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            *args,
            **kwargs,
        )
        self.meta["is_complete"] = self.check_completeness(log_level=None)  # type: ignore

        if name is not None:
            self.meta["name"] = name  # type: ignore
        if file_name is not None:
            self.meta["full_file_name"] = file_name  # type: ignore
            try:
                self.meta.update(parse_and_format_exofop_file_name(file_name))  # type: ignore
            except Exception as e:
                logger.warning(f"Could not parse file name {file_name}. Error: {e}")

    @property
    def synonym_map(self) -> SynonymMapLc:
        return self._synonym_map

    @property
    def time(self):
        """The time column of the observation."""
        if self.synonym_map.light_curve_attributes.time in self.colnames:
            return self[self.synonym_map.light_curve_attributes.time]
        else:
            logger.warning(
                f"Time column not found in observation {self.name}. Light curve is incomplete."
                " Standardise column names first."
            )
            return None

    @time.setter
    def time(self, value):
        self[self.synonym_map.light_curve_attributes.time] = value

    @property
    def flux(self):
        """The flux column of the observation."""
        if self.synonym_map.light_curve_attributes.flux in self.colnames:
            return self[self.synonym_map.light_curve_attributes.flux]
        else:
            logger.warning(
                f"Flux column not found in observation {self.name}. Light curve is incomplete."
                " Standardise column names first."
            )
            return None

    @flux.setter
    def flux(self, value):
        self[self.synonym_map.light_curve_attributes.flux] = value

    @property
    def flux_err(self):
        """The flux error column of the observation."""
        if self.synonym_map.light_curve_attributes.flux_err in self.colnames:
            return self[self.synonym_map.light_curve_attributes.flux_err]
        else:
            logger.warning(
                f"Flux error column not found in observation{self.name}. Light curve is incomplete."
                " Standardise column names first."
            )
            return None

    @flux_err.setter
    def flux_err(self, value):
        self[self.synonym_map.light_curve_attributes.flux_err] = value

    @property
    def name(self):
        """The name of the observation. Synonym of `observation_name`.

        See Also
        --------
        exofop.extract.LightCurveTable.observation_name
        """
        if self.meta.get("name", None) is None:
            return self.meta.get("full_file_name", None)

        return self.meta.get("name", None)

    @name.setter
    def name(self, value):
        self.meta["name"] = value

    @property
    def observation_name(self):
        """The name of the observation. Synonym of `name`.

        See Also
        --------
        exofop.extract.LightCurveTable.name
        """
        return self.meta.get("name", None)

    @observation_name.setter
    def observation_name(self, value):
        self.meta["name"] = value

    @property
    def file_name(self):
        """The measurement filename of the observation."""
        return self.meta.get("full_file_name", None)

    @file_name.setter
    def file_name(self, value):
        self.meta["full_file_name"] = value

    @property
    def is_complete(self) -> bool:
        """A boolean indicating whether the table is complete and non-degenerate."""
        return self.meta.get("is_complete", False)

    @is_complete.setter
    def is_complete(self, value):
        self.meta["is_complete"] = value

    def check_completeness(
        self, synonym_map: Optional[SynonymMapLc] = None, log_level: Optional[int] = 20
    ) -> bool:
        """
        Check if a complete light curve is contained in the table.

        Parameters:
        -----------
        synonym_map : SynonymMapLc
            An object representing the synonym map for the Table columns.
        log_level : int, optional
            The log level for logging missing columns (default is 20, i.e. 'info').

        Returns:
        -----------
        bool
            A boolean indicating whether the Table is complete and non-degenerate.
        """
        if synonym_map is None:
            synonym_map = self.synonym_map

        missing_columns = [
            item for item in synonym_map.light_curve_attributes if item not in self.colnames
        ]
        is_complete = not missing_columns

        if not is_complete and isinstance(log_level, int):
            logger.log(
                log_level,
                f"Observation '{self.name}' is incomplete or not in standard form. "
                f"Missing column(s): {missing_columns}. ",
            )
            logger.log(
                log_level,
                f"Columns present in '{self.name}': "
                + (f"{self.colnames[:30]} ..." if len(self.colnames) > 30 else f" {self.colnames}"),
            )

        return is_complete

    def cbvs(self, synonym_map: Optional[SynonymMapLc] = None) -> "LightCurveTable":
        """Get the cotrending basis vectors (CBVs) contained in a standardized table.

        This is a convenience function to get the CBVs, i.e. all primary aliases of
        `synonym_map` that do not represent time, flux or flux_err.

        Parameters
        ----------
        synonym_map : SynonymMapLc, optional
            A synonym map for the column names (default is None).

        Returns
        -------
        LightCurveTable
            A table containing the CBVs.

        Notes
        -----
        This function assumes that the table is already standardised, otherwise it might return
        an incomplete set of CBVs.

        See Also
        --------
        exofop.extract.LightCurveTable.light_curve
        """
        if synonym_map is None:
            synonym_map = self.synonym_map

        contained_cbvs = [item for item in self.synonym_map.cbv_names if item in self.colnames]
        return self[contained_cbvs]

    def light_curve(self, synonym_map: Optional[SynonymMapLc] = None) -> "LightCurveTable":
        """Get the light curve contained in a standardised table, i.e. the time, flux and flux_err columns.

        Parameters
        ----------
        synonym_map : SynonymMapLc, optional
            A synonym map for the column names (default is None).

        Returns
        -------
        LightCurveTable
            A table containing the light curve data.

        Notes
        -----
        This function assumes that the table is already standardised, otherwise it might return
        an incomplete set of CBVs.

        See Also
        --------
        exofop.extract.LightCurveTable.cbvs
        """
        if synonym_map is None:
            synonym_map = self.synonym_map

        if not self.check_completeness(synonym_map=synonym_map):
            raise ValueError("Light curve is incomplete. Standardise column names first.")

        return self[synonym_map.light_curve_attributes]

    @classmethod
    def from_pandas(
        cls,
        data_frame: pd.DataFrame,
        name: Optional[str] = None,
        file_name: Optional[str] = None,
        meta: Optional[dict] = None,
        **kwargs,
    ):
        """
        Create a LightCurveTable from a pandas DataFrame.

        Parameters
        ----------
        data_frame : pandas.DataFrame
            The DataFrame containing the light curve data.
        name : str
            The name of the observation.
        file_name : str
            The measurement filename of the observation,
            e.g. 'TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv'
            from whicht the meta data is attempted to be derived.
        **kwargs
            Additional keyword arguments to be passed to the `astropy.table.Table` constructor.
        """
        # meta = kwargs.pop('meta', None)
        tbl = super().from_pandas(data_frame, **kwargs)

        return cls(tbl, name=name, file_name=file_name, meta=meta)

    def standardise_column_names(
        self,
        synonym_map: Optional[Union[SynonymMap, dict]] = None,
        inplace: bool = True,
        log_level: Optional[int] = 20,
    ):
        """Renames the columns of the table according to the synonym map."""
        if synonym_map is None:
            synonym_map = self.synonym_map
        elif isinstance(synonym_map, dict) and not isinstance(synonym_map, SynonymMap):
            synonym_map = SynonymMap()
            synonym_map = synonym_map.update(synonym_map)

        if not isinstance(synonym_map, SynonymMap):
            raise ValueError(
                "'synonym_map' must be of type `SynonymMap` or `dict`."
                f" Instead, it is of type {type(synonym_map)}."
            )

        tbl = self if inplace else self.copy()
        observation_name = tbl.name

        for primary_alias in synonym_map:
            if primary_alias not in tbl.colnames:
                contained_synonyms = [
                    key for key in synonym_map[primary_alias] if key in tbl.colnames
                ]
                if not any(contained_synonyms):
                    msg = (
                        f"None of the columns of the observation {observation_name} match the"
                        f" synonyms of `{primary_alias}`. This light curve will be incomplete. "
                        + (
                            f"Columns present: {tbl.colnames[:30]} ..."
                            if len(tbl.colnames) > 30
                            else f" Columns present: {tbl.colnames}"
                        )
                    )
                    # Log warning if primary_alias is a light curve attribute
                    logger.debug(msg)
                elif len(contained_synonyms) == 1:
                    tbl.rename_column(contained_synonyms[0], primary_alias)
                if len(contained_synonyms) > 1:
                    logger.warning(
                        f"Multiple columns of the observation {observation_name} match the"
                        f" synonyms of `{primary_alias}`."
                        f" The first one, {synonym_map[primary_alias][0]}, will be used."
                    )
                    tbl.rename_column(contained_synonyms[0], primary_alias)

        self.is_complete = self.check_completeness(
            synonym_map=synonym_map if isinstance(synonym_map, SynonymMapLc) else None,
            log_level=log_level,
        )
        if not inplace:
            return tbl

    def parse_and_format_exofop_file_name(self, file_name: Optional[str] = None) -> dict:
        if file_name is None:
            file_name = self.meta.get("full_file_name", None)

        if file_name is None:
            raise ValueError(
                "No file name provided. Please provide a file name or set it as meta data."
            )
        return parse_and_format_exofop_file_name(file_name)

    def apply_time_correction_in_case_of_discrepancy(self, time_threshold: Optional[float] = 3):
        """
        Apply time correction to the time array of a table if needed.

        This function checks for a discrepancy between the starting time of the array
        and the starting time given in the file_name_components, which was obtained by parsing the
        measurement file name. If the difference is significant, it applies a time correction
        by subtracting an integer number of days from the time array.

        Parameters
        ----------
        time_threshold : int, optional
            Threshold value for considering a time difference as significant (default is 3 days).

        Returns
        -------
        None
            The DataFrame is modified in-place.

        """
        if self.time is None:
            raise ValueError("No time column found. Please standardise column names first.")

        if "jd" not in self.meta:
            file_name_components = self.parse_and_format_exofop_file_name()
            self.meta.update(file_name_components)

        if "jd" not in self.meta:
            raise ValueError(
                "No file name components found. Please provide a valid file name, like"
                " lc.file_name="
                "'TIC254113311.01_20200805_ASTEP-ANTARCTICA_Rc_compstar-lightcurves.csv'."
            )

        if self.meta["jd"] == 0.0:  # File name components contain no time information
            logger.debug("No time correction applied. As JD is 0.0.")
            return None

        start_time_difference = float(self.meta["jd"]) - np.floor(self.time[0])

        if abs(start_time_difference) > time_threshold:
            time_correction = start_time_difference
            logger.warning(
                f"Time correction of {time_correction:.5e} days"
                f" was added to observation '{self.name}'"
            )
            logger.info(
                f"Original time: {self.time[0]:10.2f} -> "
                f"Corrected time: {self.time[0] + time_correction:10.2f}"
            )

            self.time += time_correction

    def _create_plot(self, ax=None, method="None", plt=None, **kwargs):
        if plt is None:
            try:
                import matplotlib.pyplot as plt
            except ImportError:
                logger.warning("Could not import matplotlib.")
                return None

        if not self.check_completeness():
            logger.warning(
                f"Light curve {self.name} is incomplete. Standardise column names first."
            )
            return None

        with plt.style.context(MPLSTYLE):  # type: ignore
            if ax is None:
                fig, ax = plt.subplots(1, figsize=(6.69, 4.14))

            # Determine method
            if method == "plot":
                ax.plot(self.time, self.flux, **kwargs)  # type: ignore, as lc is complete
            elif method == "errorbar":
                ax.errorbar(self.time, self.flux, self.flux_err, **kwargs)  # type: ignore
            elif method == "scatter":
                ax.scatter(self.time, self.flux, **kwargs)  # type: ignore
            else:
                raise ValueError(f"Unknown method {method}.")

            ax.set_xlabel("Time [JD]")
            ax.set_ylabel("Flux")

        return ax

    def plot(self, ax=None, **kwargs):
        return self._create_plot(ax=ax, method="plot", **kwargs)

    def errorbar(self, ax=None, **kwargs):
        return self._create_plot(ax=ax, method="errorbar", **kwargs)

    def scatter(self, ax=None, **kwargs):
        return self._create_plot(ax=ax, method="scatter", **kwargs)


class LightCurveTableList(list):
    """
    A list-like container for LightCurveTable objects with additional functionalities.

    Parameters
    ----------
    target_dir : str, optional
        The directory containing the downloaded tag directories (default is None).

    Examples
    --------
    >>> tbl_list = LightCurveTableList.load_exofop_data(
    ...     target_dir='path/to/your/directory/with/downloaded/measurements',
    ... )
    >>> tbl_list.info_df

    Notes
    -----
    This class provides a convenient way to handle multiple light curve observations.
    It is designed to be used in combination with the `LightCurveTable` class and provides
    the following functionalities:

    - Loads potentially heterogeneous measurement files from the specified directory.

    - Extracts information from measurement file names.

    - Creates or loads a summary DataFrame with information on the observations.

    - Standardizes column and index names of the measurement DataFrames.

    - Applies time corrections in case of time discrepancies between file_name and data.

    - Identifies essential columns for light curves and thus checks their completeness.

    See Also
    --------
    exofop.extract.LightCurveTable : A custom table class for representing light curve data.
    exofop.extract.SynonymMapLc : A map containing synonyms for the standardisation of column names.
    """

    _synonym_map = SYNONYM_MAP

    def __init__(self, *args, target_dir: Optional[str] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._info_df = None
        self.target_dir = target_dir
        self.standardised = False

    @property
    def synonym_map(self) -> SynonymMapLc:
        """Synonym map to standardise column names."""
        if len(self) == 0:
            return self._synonym_map
        else:
            return self[0].synonym_map

    @property
    def complete(self) -> "LightCurveTableList":
        """Subset of complete observations."""
        if not self.standardised:
            logger.warning("The column names are not standardised yet. Result may be incomplete.")
        return LightCurveTableList([item for item in self if item.is_complete])

    @property
    def incomplete(self) -> "LightCurveTableList":
        """Subset of incomplete observations."""
        if not self.standardised:
            logger.warning("The column names are not standardised yet. Result may be incomplete.")
        return LightCurveTableList([item for item in self if not item.is_complete])

    @property
    def names(self) -> List[str]:
        """Names of all observations."""
        return [item.name for item in self]

    @property
    def info_df(self) -> pd.DataFrame:
        """pandas.DataFrame summarizing information on observations."""
        if self._info_df is None:
            self._info_df = self.update_info_df()
        return self._info_df

    @property
    def time(self) -> List:
        """List of time arrays of all observations."""
        if not self.standardised:
            logger.warning("The column names are not standardised yet. Result may be incomplete.")
        return [item.time for item in self]

    def number_of_cbvs(self, synonym_map: Optional[SynonymMapLc] = None):
        """Number of CBVs for all observations."""
        if not self.standardised:
            logger.warning("The column names are not standardised yet. Result may be incomplete.")
        return [len(item.cbvs(synonym_map=synonym_map).colnames) for item in self]

    def _get_by_name(self, name: str) -> Optional[LightCurveTable]:
        if name in self.names:
            return self[self.names.index(name)]
        else:
            logger.info(f"Observation {name} is not contained.")
            return None

    def __getitem__(self, key: Union[int, str]) -> Union[LightCurveTable, None]:
        """Get an item by index or by name."""
        if isinstance(key, str):
            return self._get_by_name(key)
        else:
            return super().__getitem__(key)

    def standardise_column_names(
        self, synonym_map: Optional[Union[SynonymMap, dict]] = None, log_level: Optional[int] = 20
    ):
        """Standardise column names of all observations in the list.

        Parameters
        ----------
        synonym_map : SynonymMap or dict, optional
            A synonym map for the column names (default is None).
        log_level : int, optional
            The log level for logging missing columns (default is 20, i.e. 'info').

        See Also
        --------
        exofop.extract.LightCurveTable.apply_time_correction_in_case_of_discrepancy
        """
        for tbl in self:
            try:
                tbl.standardise_column_names(synonym_map, log_level=log_level)
            except Exception as e:
                logger.warning(
                    f"Could not standardise column names for observation {tbl.name}. Error: {e}"
                )

        incomplete_names = [item.name for item in self if not item.is_complete]

        if len(incomplete_names) > 0:
            logger.info(
                f"{len(incomplete_names)} of {len(self)} observations are incomplete."
                f" Namely: {', '.join(incomplete_names)}."
                "\n Investigate further using the `incomplete` attribute."
            )
        else:
            if isinstance(synonym_map, SynonymMapLc):
                logger.info("All observations contain a complete light curve.")

        self.standardised = True
        self.update_info_df()

    def apply_time_correction_in_case_of_discrepancy(self, time_threshold: Optional[float] = 3):
        """Apply time correction to the time array of individual observations in the list if needed.

        This function checks for a discrepancy between the starting time of the array
        and the starting time given in the file_name_components, which was obtained by parsing the
        measurement file name. If the difference is significant, it applies a time correction
        by subtracting an integer number of days from the time array.

        Parameters
        ----------
        time_threshold : int, optional
            Threshold value for considering a time difference as significant (default is 3 days).

        See Also
        --------
        exofop.extract.LightCurveTable.standardise_column_names

        """
        for tbl in self:
            try:
                tbl.apply_time_correction_in_case_of_discrepancy(time_threshold)
            except Exception as e:
                logger.warning(
                    f"Could not apply time correction for observation {tbl.name}. Error: {e}",
                    exc_info=True,
                )

        self.update_info_df()

    def missing_cbvs(self, synonym_map: Optional[SynonymMapLc] = None) -> Optional[dict]:
        """Check for missing CBVs in the observations contained in the list.

        This is a convenience function to check which CBVs are missing in which observations.

        Parameters
        ----------
        synonym_map : SynonymMapLc, optional
            A synonym map for the column names (default is None).

        Returns
        -------
        dict or None
            A dictionary containing the names of the observations and the missing CBVs.
            If all observations contain all CBVs, None is returned.

        """
        if synonym_map is None:
            synonym_map = self.synonym_map

        if not self.standardised:
            logger.warning("The column names are not standardised yet. Result may be incomplete.")

        missing_cbvs = {
            f"{tbl.name}": (
                tbl.meta["observatory"],
                [cbv for cbv in synonym_map.cbv_names if cbv not in tbl.colnames],
            )
            for tbl in self
        }

        # Remove entries with empty lists of missing CBVs
        missing_cbvs = {key: val for key, val in missing_cbvs.items() if val[1]}

        if len(missing_cbvs) > 0:
            return missing_cbvs
        else:
            return None

    def update_info_df(
        self,
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
        if self._info_df is None:
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
                    "texp",
                    "Duration",
                    "Efficiency",
                    "cbvs",
                    "ncols",
                ]
            )
        else:
            info_df = self._info_df

        for item in self:
            meta = item.meta
            info_df.loc[item.name, "Date"] = meta.get("yyyymmdd", "")
            info_df.loc[item.name, "BJD"] = int(np.floor(meta.get("jd", -1)))
            info_df.loc[item.name, "Observatory"] = meta.get("observatory", "")
            info_df.loc[item.name, "Filter"] = meta.get("filter", "")
            info_df.loc[item.name, "target"] = meta.get("target", "")
            info_df.loc[item.name, "pp"] = meta.get("pp", "")
            info_df.loc[item.name, "Measurement file name"] = (
                f"{meta.get('filetype', '')}.{meta.get('ext', '')}"
            )
            info_df.loc[item.name, "full_file_name"] = meta.get("full_file_name", "")
            info_df.loc[item.name, "cbvs"] = len(item.cbvs().colnames)
            info_df.loc[item.name, "ncols"] = len(item.colnames)

            time = item.time
            if time is not None:
                info_df.loc[item.name, "texp"] = np.median(np.diff(time)) * 24 * 1200
                info_df.loc[item.name, "Duration"] = (time[-1] - time[0]) * 24
                # N_obs/N_theory
                info_df.loc[item.name, "Efficiency"] = np.round(
                    ((len(time) - 1) * np.min(np.diff(time)) / ((time[-1] - time[0])))
                    * 100,  # in percent
                    decimals=1,
                )
        info_df["BJD"] = info_df["BJD"].astype(int)
        info_df["pp"] = info_df["pp"].astype(int)

        return info_df

    @property
    def default_save_dir(self) -> Optional[str]:
        """Default directory for saving the data, namely target_dir/output."""
        if self.target_dir is not None:
            save_dir = os.path.join(self.target_dir, "output")
            os.makedirs(save_dir, exist_ok=True)
            return save_dir
        else:
            return None

    def save(self, save_dir: Optional[str] = None):
        """Save the LightCurveTableList to a directory.

        Parameters
        ----------
        save_dir : str, optional
            The directory where the data should be saved. Defaults to the target_dir.

        Notes
        -----
        The data is saved in the following format:
        - The info DataFrame is saved to a file 'info.csv'.
        - Each observation is saved to a file 'observation_name.ecsv'.
        - The observation names are used as file names.

        See Also
        --------
        exofop.extract.LightCurveTableList.load : Load the data from a directory.
        """
        if save_dir is None:
            save_dir = self.default_save_dir

        if save_dir is None:
            raise ValueError("Please provide a save directory.")

        self.info_df.to_csv(os.path.join(save_dir, "info.csv"))

        for tbl in self:
            tbl.write(os.path.join(save_dir, tbl.name + ".ecsv"), overwrite=True)
            # tbl.write(os.path.join(save_dir, tbl.name + ".fits"), overwrite=True)

    @classmethod
    def load(cls, load_dir: str = ".") -> "LightCurveTableList":
        """Load the LightCurveTableList from a directory.

        Parameters
        ----------
        load_dir : str, optional
            The directory from which the data should be loaded (default is '.').

        Returns
        -------
        LightCurveTableList
            The loaded LightCurveTableList.

        Notes
        -----
        You can modify the info.csv file to remove observations from being loaded,
        e.g. if they are incomplete, corrupted or superfluous.

        See Also
        --------
        exofop.extract.LightCurveTableList.save : Soad the data from a directory.
        """
        info_df = pd.read_csv(os.path.join(load_dir, "info.csv"), index_col=0)

        tbl_list = []
        for name in info_df.index:
            try:
                tbl = LightCurveTable.read(
                    os.path.join(load_dir, f"{name}.ecsv"), format="ascii.ecsv"
                )
                # tbl = LightCurveTable.read(os.path.join(load_dir, name + ".fits"))
            except Exception as e:
                logger.warning(f"Could not load observation {name}. Error: {e}")
                continue
            tbl_list.append(tbl)

        tbl_list = cls(tbl_list)
        tbl_list._info_df = info_df
        return tbl_list

    def save_to_pickle(self, file_name: Optional[str] = None):
        """Save the instance to a file using pickle serialization."""
        import pickle

        if file_name is None and self.target_dir is not None:
            file_name = self.target_dir + "output.pkl"
        else:
            raise ValueError("Please provide a file name.")

        with open(file_name, "wb") as file:
            pickle.dump(self, file, pickle.HIGHEST_PROTOCOL)

    @classmethod
    def load_from_pickle(cls, file_path) -> "LightCurveTableList":
        """Load an instance from a saved file."""
        import pickle

        with open(file_path, "rb") as file:
            loaded_instance = pickle.load(file)
        if isinstance(loaded_instance, cls):
            return loaded_instance
        else:
            raise ValueError("Loaded object is not an instance of StandardisedExofopData")

    def __repr__(self):
        return f"LightCurveTableList({[item.name for item in self]})"

    @classmethod
    def load_exofop_data(
        cls,
        target_dir: str,
        observation_names: Optional[List[str]] = None,
        synonym_map_lc: SynonymMapLc = SYNONYM_MAP_LC,
        allow_multiple_filetypes=True,
        **kwargs,
    ) -> "LightCurveTableList":
        """
        Load and standardize ExoFOP data for a given system.

        Parameters
        ----------
        target_dir : str
            The directory where the ExoFOP  data of the given system is stored.

        observation_names : List[str], optional
            A list of observation names to consider. If not provided, the function
            will use all available observations sorted by tag.

        time_threshold : int, optional
            A threshold for applying time corrections to data in case of discrepancies
            in time specifications between the file name and the data in units of days,
            default is 3.

        Returns
        -------
        LightCurveTableList
            A list of LightCurveTables containing the ExoFOP data extracted from target_dir.

        Notes
        -----
        This function loads and standardizes ExoFOP data for specific planets. It performs
        the following steps:

        1. Loads potentially heterogeneous measurement files from the specified directory.

        2. Extracts information from measurement file names.

        3. Unpacks multiple measurements from the same tag into separate observations.


        Examples
        --------
        >>> target_dir = '/path/to/data'
        >>> observation_names = None
        >>> synonym_map_lc = SYNONYM_MAP_LC
        >>> allow_multiple_filetypes = True
        >>> exofop_data = LightCurveTableList.load_exofop_data(
        ...     target_dir=target_dir,
        ...     observation_names=observation_names,
        ...     synonym_map_lc=synonym_map_lc,
        ...     allow_multiple_filetypes=allow_multiple_filetypes,
        ... )
        >>> exofop_data

        """
        # Observation_names have to be sorted.
        # apply_time_corrections_to_dfs_in_case_of_discrepancy can cause problems otherwise.
        if observation_names is None:
            observation_names = get_sorted_exofop_observation_list(target_dir)
        else:
            observation_names = sorted(observation_names, key=extract_number_for_sort)

        logger.debug(f"Loading data for observations: {observation_names} in {target_dir}")
        # Load potentially heterogenous measurement files downloaded from exofop stored in folders
        # with names observation_names, which could for example be the tag name of the file
        unformatted_df_dict, measurement_file_names = load_exofop_measurement_files_as_dfs(
            observation_names,
            target_dir,
            infer_separator=True,
            essential_attribute_names=synonym_map_lc.light_curve_attributes,
        )

        # Extract information from exofop measurement file names
        logger.debug("Extracting information from file names.")
        file_name_components_dict = extract_components_from_exofop_measurement_file_names(
            unformatted_df_dict, measurement_file_names
        )

        unpack_multiple_measurements_from_same_tag(
            file_name_components_dict=file_name_components_dict,
            unformatted_df_dict=unformatted_df_dict,
            allow_multiple_filetypes=allow_multiple_filetypes,
        )

        # Remove leading or trailing white spaces from column names
        for df in unformatted_df_dict.values():
            df.rename(columns=lambda x: x.strip(), inplace=True)

        tbl_list = cls(
            [
                LightCurveTable.from_pandas(df, name=key, meta=file_name_components_dict[key])
                for key, df in unformatted_df_dict.items()
            ],
            target_dir=target_dir,
        )

        # for tbl in tbl_list:
        #     tbl.standardise_column_names(synonym_map_lc=synonym_map_lc)

        #     # Apply time correction to the time array of a DataFrame in case of discrepancy
        #     # between the time specified in the measurement and the one given in the file_name
        #     tbl.apply_time_correction_in_case_of_discrepancy(time_threshold=time_threshold)

        return tbl_list


def unpack_multiple_measurements_from_same_tag(
    file_name_components_dict, unformatted_df_dict, allow_multiple_filetypes=True
):
    """Unpack multiple measurements from the same tag into separate observations.

    Unpacks multiple measurements from the same tag into separate dataframes and updates the dictionaries
    containing file name components and unformatted dataframes accordingly.

    Parameters
    ----------
    file_name_components_dict : dict
        A dictionary containing observation names and corresponding file name components.
    unformatted_df_dict : dict
        A dictionary containing observation names and corresponding unformatted dataframes.
    allow_multiple_filetypes : bool, optional
        A boolean indicating whether to allow multiple file types (default is True).
    """
    pattern = re.compile("|".join(["measurements", "measurement", "lightcurves"]), re.IGNORECASE)

    for key, val in file_name_components_dict.copy().items():
        if isinstance(val, list):
            if len(val) == 0:
                logger.error(f"No file name components found for observation {key}.")

            # Observations from different filters were published in the same tag
            if len({item["filter"] for item in val}) == len(val):
                filter_names = [item["filter"] for item in val]
                for ind, item in enumerate(val):
                    filter_name = item["filter"]
                    unformatted_df_dict[key + "_" + filter_name] = unformatted_df_dict[key][ind]
                    file_name_components_dict[key + "_" + filter_name] = item
                del unformatted_df_dict[key]
                del file_name_components_dict[key]
                logger.info(
                    f"Multiple measurement files from different filters found for observation {key}."
                    f" Namely: {filter_names}."
                )
            elif all("_" in item["filetype"] for item in val) and allow_multiple_filetypes:
                measurement_file_names = [item["filetype"] for item in val]
                for ind, item in enumerate(val):
                    # Typical cases are mask size, e.g. 3px_Measurements.tbl
                    # Remove 'measurement', 'measurements' or 'lightcurves' from the file type
                    new_name = (
                        key
                        + "_"
                        + re.sub(
                            "_+",
                            "_",
                            pattern.sub("", item["filetype"]).removeprefix("_").removesuffix("_"),
                        )
                    )

                    unformatted_df_dict[new_name] = unformatted_df_dict[key][ind]
                    file_name_components_dict[new_name] = item
                del unformatted_df_dict[key]
                del file_name_components_dict[key]
                logger.info(
                    f"Multiple measurement files found for observation {key}."
                    f" Namely: {measurement_file_names}."
                )
            elif allow_multiple_filetypes:
                measurement_file_names = [item["full_file_name"] for item in val]
                for ind, item in enumerate(val):
                    file_name = item["full_file_name"].split(".")[0]
                    unformatted_df_dict[key + "_" + file_name] = unformatted_df_dict[key][ind]
                    file_name_components_dict[key + "_" + file_name] = item
                del unformatted_df_dict[key]
                del file_name_components_dict[key]
                logger.info(
                    f"Multiple files found for observation {key},"
                    " non of which following standard naming conventions."
                    f" Namely: {measurement_file_names}."
                )
            else:
                # Delete the observation from the dictionary
                del unformatted_df_dict[key]
                del file_name_components_dict[key]


def get_sorted_exofop_observation_list(data_dir):
    """
    Get a sorted list of observation tags from a directory containing datasets.
    Directories named 'zip' and 'output' are ignored.

    Parameters
    ----------
    data_dir : str
        The directory containing dataset subdirectories.

    Returns
    -------
    list of str
        A sorted list of observation tags.

    Example
    -------
    >>> data_dir = '/path/to/data'
    >>> observation_list = get_sorted_observation_list(data_dir)
    """

    observation_list = [
        tag
        for tag in os.listdir(data_dir)
        if os.path.isdir(os.path.join(data_dir, tag))
        if tag != "zip" and tag != "output"
    ]
    observation_list = sorted(observation_list, key=extract_number_for_sort)

    logger.info(f'Tags of datasets processed: {" ".join(observation_list)}')

    return observation_list


def extract_number_for_sort(s):
    """
    Extract a numerical value and trailing letters from a string for pseudo-numeric sorting.

    This function is designed to facilitate the pseudo-numeric sorting of strings that consist of
    a number followed by optional trailing letters. By dividing the input string into the numeric
    part and the remaining letters, it enables a list of such strings to be sorted in a way that
    resembles numeric sorting.

    Parameters
    ----------
    s : str
        Input string containing a numeric value followed by optional letters.

    Returns
    -------
    float or inf
        Extracted numeric value. Returns float('inf') if no numeric value is present.
    str
        Trailing letters extracted from the input string.

    Examples
    --------
    >>> extract_number_for_sort('19914B')
    (19914.0, 'B')
    >>> extract_number_for_sort('ABC')
    (inf, 'ABC')
    """
    num, letters = re.match(r"(\d*)(.*)", s).groups()
    return float(num or "inf"), letters
