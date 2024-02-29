import re
import time
from functools import wraps
from typing import Optional, Union
import logging

import httpx
import pandas as pd

from exofop.utils.urls import BASE_URL

logger = logging.getLogger("exofop.download")


class InvalidTICError(ValueError):
    def __init__(self, message="", id=None):
        default_message = "Invalid TIC ID. " if id is None else f"Invalid TIC ID: `{id}`. "
        default_message += (
            "TIC ID must be an integer or a string that can be converted to an integer. "
            "The inter must have a length of 9 digits. "
            "Examples: '123456789', 'TIC-123456789', 'TIC_123456789', 'TIC 123456789'."
        )
        super().__init__(default_message + "" + message if message else "")


class TIC:
    """
    TESSS Input Catalogue (TIC) class for handling and validating TIC IDs.

    Parameters
    ----------
    tic_id : Union[str, int]
        The TIC ID to initialize the TIC object.

    Examples
    --------
    Initialize TIC with a valid TIC ID

    >>> tic = TIC(123456789)
    >>> tic.id
    '123456789'

    Initialize TIC with a valid TIC ID as a string

    >>> tic_str = TIC('231663901')
    >>> tic_str.to_toi()
    TOI(101)

    Initialize TIC with an invalid TIC ID (raises InvalidTICError)

    >>> invalid_tic = TIC('invalid_id')  # doctest: +SKIP
    Traceback (most recent call last):
    InvalidTICError: Invalid TIC ID: `invalid_id` ...

    Alternatively, you can use the exists method to check if a TIC ID is valid

    >>> TIC('123456789').exists()
    False

    """

    def __init__(self, tic_id: Union[str, int, "TIC"]):
        if isinstance(tic_id, TIC):
            tic_id = tic_id.id
        self._tic_id = self._clean_id(tic_id)
        self._raise_if_invalid(input_id=tic_id)

    @property
    def id(self) -> str:
        """The TESSS Input Catalogue (TIC) ID.

        This is a string of 9 digits, e.g., "123456789".
        """
        return self._tic_id

    @staticmethod
    def _clean_id(tic_id: Union[str, int]) -> str:
        """
        Make sure that the TESSS Input Catalogue (TIC) ID is clean.
        """
        if not isinstance(tic_id, (str, int)):
            raise TypeError("TIC ID must be a string or integer.")

        if isinstance(tic_id, int):
            return str(tic_id)
        if str(tic_id).isdigit():
            return str(tic_id)

        try:
            if isinstance(tic_id, str):
                tic_id_tmp = (
                    tic_id.lower().replace("tic", "").replace("-", "").replace("_", "").strip()
                )
                # See if it could be converted to an integer
                int(tic_id_tmp)
                tic_id = tic_id_tmp
        except ValueError as e:
            raise InvalidTICError(f"Original exception: {e}", id=tic_id) from e

        return tic_id

    @staticmethod
    def _has_valid_format(tic_id: str) -> bool:
        """
        Verify that the TESSS Input Catalogue (TIC) ID is valid.
        """
        if len(tic_id) > 9 or not tic_id.isdigit():
            return False

        return True

    def lookup(self, overview_table: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """Look up the system in the overview table."""
        # Fetch the overview table if not provided (this is usually rather slow the first time)
        if overview_table is None:
            overview_table = fetch_overview_table(BASE_URL)

        # Filter the overview_table to get rows that match the TOI
        filtered_rows = overview_table[overview_table["TIC ID"] == int(self.id)]
        if filtered_rows.empty:
            logger.warning(f"TIC {self._tic_id} not found in overview table.")

        return filtered_rows

    def to_toi(self, overview_table: Optional[pd.DataFrame] = None) -> "TOI":
        """Convert TIC to TOI ID."""
        filtered_rows = self.lookup(overview_table=overview_table)
        if filtered_rows.empty:
            raise ValueError(f"TIC {self._tic_id} not found in overview table.")
        else:
            return TOI(str(str(filtered_rows["TOI"].values[0])).split(".")[0])

    def _raise_if_invalid(self, input_id=None) -> None:
        """
        Verify that the TESSS Input Catalogue (TIC) ID is valid.
        """
        if not self._has_valid_format(self._tic_id):
            raise InvalidTICError(id=self._tic_id if input_id is None else input_id)

    def exists(self, overview_table: Optional[pd.DataFrame] = None) -> bool:
        """Check if the system exists in the overview table."""
        if self.lookup(overview_table).empty:
            return False
        return True

    def __repr__(self) -> str:
        return f"TIC({self._tic_id})"

    def __str__(self) -> str:
        return f"TIC_{self._tic_id}"


class InvalidTOIError(ValueError):
    def __init__(self, message="", id=None):
        default_message = "Invalid TOI ID. " if id is None else f"Invalid TOI ID: `{id}`. "
        default_message += (
            "TOI ID must be an integer or a string that can be converted to an integer, "
            "or a float, if the TOI ID has a planet number. "
            "Examples: 'TOI1234', 'TOI-1234', 'TOI_1234', '1234.01'."
        )
        super().__init__(default_message + " " + message if message else default_message)


class TOI:
    """
    TESS Objects of Interest (TOI) class for handling and validating TOI IDs.

    Parameters
    ----------
    toi_id : Union[str, int]
        The TOI ID to initialize the TOI object.

    Examples
    --------
    Initialize TOI with a valid TOI ID

    >>> toi = TOI(1234)
    >>> toi.id
    'TOI1234'

    Initialize TOI with a valid TOI ID as a string

    >>> toi_str = TOI('1234')
    >>> toi_str.to_tic()
    TIC(90504905)

    Initialize TOI with an invalid TOI ID (raises InvalidTOIError)

    >>> invalid_tic = TOI('invalid_id')  # doctest: +SKIP
    Traceback (most recent call last):
    InvalidTOIError: Invalid TOI ID: `invalid_id` ...

    Alternatively, you can use the exists method to check if a TOI ID is valid

    >>> TOI('101').exists()
    True

    """
    
    def __init__(self, toi_id: Union[str, int, float, "TOI"]):
        if isinstance(toi_id, TOI):
            toi_id = toi_id.id
        self._toi_id = self._clean_id(toi_id)
        self._raise_if_invalid(input_id=toi_id)

    @property
    def id(self) -> str:
        """The TESS Objects of Interest (TOI) ID."""
        return f"TOI{self._toi_id}"

    @property
    def system(self) -> str:
        """TOI ID of the system without the planet number."""
        return self._toi_id.split(".")[0]

    @property
    def planet(self) -> str:
        """The planet number of the TESS Objects of Interest (TOI) ID."""
        toi_split = self._toi_id.split(".")
        if len(toi_split) == 1:
            return ""
        return self._toi_id.split(".")[1]

    @staticmethod
    def _clean_id(toi_id: Union[str, int, float]) -> str:
        """ Make sure that the TESS Objects of Interest (TOI) ID is clean. """
        if not isinstance(toi_id, (str, int, float)):
            raise TypeError("TOI ID must be a string or integer.")

        if isinstance(toi_id, int):
            return str(toi_id)
        if isinstance(toi_id, float):
            return str(round(toi_id, 3))

        if str(toi_id).isdigit():
            return str(toi_id)

        try:
            if isinstance(toi_id, str):
                toi_id_tmp = (
                    toi_id.lower().replace("toi-", "").replace("-", "").replace("_", "").strip()
                )
                if not toi_id_tmp.isdigit():
                    toi_id_tmp = "".join(filter(lambda char: char.isdigit() or char == ".", toi_id))
                float(toi_id_tmp)
                toi_id = toi_id_tmp
        except ValueError as e:
            raise InvalidTOIError(f"Original exception: {e}", id=toi_id) from e

        return toi_id

    @staticmethod
    def _has_valid_format(toi_id: str) -> bool:
        """
        Verify that the TESS Objects of Interest (TOI) ID is valid.
        """
        return toi_id.isdigit() or (
            len(toi_id.split(".")) > 1
            and toi_id.split(".")[0].isdigit()
            and toi_id.split(".")[1].isdigit()
        )

    def _raise_if_invalid(self, input_id=None) -> None:
        """
        Verify that the TESS Objects of Interest (TOI) ID is valid.
        """
        if not self._has_valid_format(self._toi_id):
            raise InvalidTOIError(id=self._toi_id if input_id is None else input_id)

    def lookup(self, overview_table: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """Look up the system in the overview table."""
        # Fetch the overview table if not provided (this is usually rather slow the first time)
        if overview_table is None:
            overview_table = fetch_overview_table(BASE_URL)

        # Filter the overview_table to get rows that match the TOI
        if self.planet:
            filtered_rows = overview_table[overview_table["TOI"] == self._toi_id]
        else:
            filtered_rows = overview_table[
                overview_table["TOI"].astype(float).astype(int) == int(self.system)
            ]
        if filtered_rows.empty:
            logger.warning(f"TOI {self._toi_id} not found in overview table.")

        return filtered_rows

    def exists(self, overview_table: Optional[pd.DataFrame] = None) -> bool:
        """Check if the system exists in the overview table."""
        if self.lookup(overview_table).empty:
            return False
        return True

    def to_tic(self, overview_table: Optional[pd.DataFrame] = None) -> TIC:
        """Convert TOI to TIC ID."""
        filtered_rows = self.lookup(overview_table=overview_table)
        if filtered_rows.empty:
            raise ValueError(f"TOI {self._toi_id} not found in overview table.")
        else:
            return TIC(str(str(filtered_rows["TIC ID"].values[0])))

    def __repr__(self) -> str:
        return f"TOI({self._toi_id})"

    def __str__(self) -> str:
        return f"TOI{self._toi_id}"


class System:
    """
    System class for handling and validating TIC and TOI IDs.

    Attributes
    ----------
    name : str
        The name of the system.
    tic : TIC
        The TIC ID of the system.
    toi : TOI
        The TOI ID of the system.

    Examples
    --------
    Initialize System with a TIC ID or TOI ID
    by explicitly providing a name and a TIC or TOI ID

    >>> s = System(name="cool_system", tic="254113311", toi=None)

    As the first argument is name, we can also hand IDs using the prefixes 'TIC' or 'TOI'.

    >>> s = System(name="TOI-1130")  # Indicate TOI ID with prefix 'TOI'
    >>> s = System("TIC_254113311")  # Indicate TIC ID with prefix 'TIC'

    Less recommended way, as it requires an extra lookup

    >>> System(name="1130")
    System(name=1130, tic=TIC_254113311 toi=TOI1130)

    Initialize System with a TIC ID or TOI ID and autocomplete

    >>> System(name="cool_system", tic="254113311", complete=True)
    System(name=cool_system, tic=TIC_254113311 toi=TOI1130)

    Get target ID, which can be used to query ExoFOP time series data

    >>> System(toi="TOI-1130").target
    'TOI1130'
    >>> System(tic="TIC_254113311").target
    '254113311'
    """

    def __init__(
        self,
        name: Optional[str] = None,
        tic: Optional[Union[str, int, "TIC"]] = None,
        toi: Optional[Union[str, int, float, "TOI"]] = None,
        complete: bool = False,
    ) -> None:
        self.name = name

        if toi is None and tic is None and name is None:
            raise ValueError("Either `tic` or `toi` must be provided.")
        elif toi is None and tic is None:
            self._infer_from_name(name)
        else:
            self.tic = None if tic is None else TIC(tic)
            self.toi = None if toi is None else TOI(toi)

            if self.name is None:
                if toi is not None:
                    self.name = str(self.toi)
                elif tic is not None:
                    self.name = str(self.tic)

        if complete:
            self.autocomplete()

    @property
    def target(self) -> str:
        """The target ID of the system. This is either the TIC or TOI ID."""
        if self.toi is not None:
            return self.toi.id
        if self.tic is not None:
            return self.tic.id
        else:
            raise ValueError("Either `tic` or `toi` must be provided.")

    def get_toi(self) -> TOI:
        """Get the TOI ID of the system."""
        if self.toi is not None:
            return self.toi
        else:
            self.autocomplete()
            assert self.toi is not None
            return self.toi

    def get_tic(self) -> TIC:
        """Get the TIC ID of the system."""
        if self.tic is not None:
            return self.tic
        else:
            self.autocomplete()
            assert self.tic is not None
            return self.tic

    def autocomplete(self) -> bool:
        """Autocomplete the system by inferring the missing TIC or TOI ID from the provided one."""
        if self.tic is not None and self.toi is None:
            self.toi = self.tic.to_toi()
        elif self.toi is not None and self.tic is None:
            self.tic = self.toi.to_tic()
        else:
            return True

        return self.is_complete()

    def lookup(self, overview_table: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """Look up the system in the overview table."""
        if self.tic is not None:
            return self.tic.lookup(overview_table)
        elif self.toi is not None:
            return self.toi.lookup(overview_table)
        else:
            raise ValueError("Either `tic` or `toi` must be provided.")

    def exists(self, overview_table: Optional[pd.DataFrame] = None) -> bool:
        """Check if the system exists in the overview table."""
        if self.tic is not None:
            return self.tic.exists(overview_table)
        elif self.toi is not None:
            return self.toi.exists(overview_table)
        else:
            raise ValueError("Either `tic` or `toi` must be provided.")

    def is_complete(self) -> bool:
        """Check if the system is complete, i.e., if both TIC and TOI IDs are provided."""
        if self.tic is not None and self.toi is not None:
            return True
        return False

    def is_consistent(self) -> bool:
        """Check if both TIC and TOI IDs are referring to the same system."""
        if not self.is_complete():
            return True

        if self.tic is not None and self.toi is not None and (self.tic.to_toi().id != self.toi.id):
            return False

        return True

    def _raise_if_invalid(self) -> None:
        if self.tic is not None and not self.tic._has_valid_format(self.tic.id):
            raise InvalidTICError(id=self.tic.id)
        if self.toi is not None and not self.toi._has_valid_format(self.toi.id):
            raise InvalidTOIError(id=self.toi.id)

    def _infer_from_name(self, name):
        self.tic = None
        self.toi = None

        if "toi" in name.lower():
            self.toi = TOI(name)
        elif "tic" in name.lower():
            self.tic = TIC(name)
        else:
            success = False
            logger.info(f"Target ambiguous. Trying to infer TIC or TOI ID from `{name}`.")
            try:
                self.toi = TOI(name)
                success = self.toi.exists()
            except InvalidTOIError:
                self.toi = None
                try:
                    self.tic = TIC(name)
                    success = self.tic.exists()
                except InvalidTICError:
                    pass

            if success:
                self.autocomplete()
            if not success:
                raise ValueError(
                    f"Could not convert `{name}` to either a TIC or TOI ID."
                    f"Provide either a TIC or TOI ID."
                )

    def __repr__(self) -> str:
        return "System(" f"name={self.name}, tic={self.tic} " f"toi={self.toi}" ")"


def cache_log_once(func):
    """Cache the results of a function and log the time it took to download the data."""
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs):

        if args not in cached_results:
            logger.info(
                "Downloading TOI overview table from ExoFOP, to convert between TIC and TOI IDs. "
                "This may take a while the first time, but will be cached for future use."
            )
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time

            logger.info(f"Downloading TOI overview table took {elapsed_time:.2f} seconds.")

            cached_results[args] = result

        return cached_results[args]

    return wrapper


@cache_log_once
def fetch_overview_table(base_url: str = BASE_URL) -> pd.DataFrame:
    """
    Fetch the TESS Target Of Interest (TOI) overview table from a specified base URL.

    Parameters
    ----------
    base_url : str
        The base URL for fetching the TOI overview table.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame containing the TOI overview table.

    Examples
    --------
    >>> overview_table = fetch_overview_table(BASE_URL)
    >>> print(overview_table.head())  # doctest: +SKIP
          TIC ID  Imaging Observations  ...  Date Modified (by ExoFOP-TESS)  editpri
    0   50365310                     5  ...                      2022-12-14  1000.01
    1   88863718                     5  ...                      2023-04-04  1001.01
    2  124709665                     5  ...                      2022-12-14  1002.01
    3  106997505                     1  ...                      2022-12-14  1003.01
    4  238597883                     1  ...                      2023-03-24  1004.01
    <BLANKLINE>
    [5 rows x 63 columns]
    
    """
    overview_table = fetch_tois_data()
    if overview_table is None:
        logger.warning("Failed to fetch TOI overview table fast.")
        overview_table = pd.read_csv(f"{base_url}/tess/download_toi.php?output=pipe", delimiter="|")

    return overview_table


def fetch_tois_data():
    """Fetch TOI overview table from ExoFOP.

    This is a faster way to fetch the TOI overview table, but it might not be as reliable.
    """
    # Dictionary to rename columns
    # Generated using `get_column_dictionary()`
    rename_dict = {
        "ticid": "TIC ID",
        "toi": "TOI",
        "ctoival": "CTOI",
        "master_priority": "Master priority",
        "sg1a_priority": "SG1A priority",
        "sg1b_priority": "SG1B priority",
        "sg2_priority": "SG2 priority",
        "sg3_priority": "SG3 priority",
        "sg4_priority": "SG4 priority",
        "sg5_priority": "SG5 priority",
        "acwg_priority": "ACWG priority",
        "acwg_esm": "ESM",
        "acwg_tsm": "TSM",
        "acwg_ckmass": "Predicted Mass (M_Earth)",
        "numtseries": "Time Series Observations",
        "numspect": "Spectroscopy Observations",
        "numimaging": "Imaging Observations",
        "disposition": "TESS Disposition",
        "tfopwg_disposition": "TFOPWG Disposition",
        "tfopwg_disposition_viewedit": "View all TFOPWG Disposition",
        "tess_mag": "TESS mag",
        "tess_mag_error": "TESS mag error",
        "num_pc": "Pipeline Signal ID",
        "source": "Source",
        "detection": "Detection",
        "ra": "RA (deg)",
        "dec": "Dec (deg)",
        "pm_ra": "PM RA (mas/yr)",
        "pmra_e": "PM RA error",
        "pm_dec": "PM Dec (mas/yr)",
        "pmdec_e": "PM Dec error",
        "epoch": "Transit Epoch (BJD)",
        "epoch_e": "Transit Epoch error",
        "period": "Period (days)",
        "period_e": "Period error",
        "duration": "Duration (hours)",
        "duration_e": "Duration error",
        "depth_mmag": "Depth (mmag)",
        "depth1_e": "Depth (mmag) error",
        "depth_ppm": "Depth (ppm)",
        "depth2_e": "Depth (ppm) error",
        "planet_radius": "Planet Radius (R_Earth)",
        "prad_e": "Planet Radius error",
        "planet_insolation": "Planet Insolation (Earth flux)",
        "planet_eqtemp": "Planet Eq Temp (K)",
        "planet_snr": "Planet SNR",
        "stellar_distance": "Stellar Distance (pc)",
        "d_e": "Stellar Distance error",
        "stellar_teff": "Stellar Teff (K)",
        "teff_e": "Stellar Teff error",
        "stellar_logg": "Stellar log(g) (cm/s2)",
        "logg_e": "Stellar log(g) error",
        "stellar_radius": "Stellar Radius (R_Sun)",
        "srad_e": "Stellar Radius error",
        "mh": "Stellar Metallicity",
        "mh_e": "Stellar Metallicity error",
        "mass": "Stellar Mass (M_Sun)",
        "mass_e": "Stellar Mass error",
        "sectors": "Sectors",
        "comments": "Comments",
        "date_toi_alerted": "Date TOI Alerted (by TESS Project)",
        "date_toi_edited": "Date TOI Updated (by TESS Project)",
        "date_modified": "Date Modified (by ExoFOP-TESS)",
    }

    url = "https://exofop.ipac.caltech.edu/tess/json/tois.json"

    response = httpx.get(url)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data)
        # rename_dict = get_column_dictionary()
        return df.rename(columns=rename_dict)
    else:
        return None


def get_column_dictionary():
    """Get the column dictionary for the TOI overview table."""
    url = f"{BASE_URL}/tess/view_toi.php"

    # Send a GET request to the webpage
    response = httpx.get(url)

    # Extract JavaScript code containing column definitions using regex
    column_defs_regex = re.findall(r"var\s+columnDefs\s*=\s*(\[.*?\]);", response.text, re.DOTALL)[
        0
    ]

    pattern = r'headerName:\s*"([^"]+)",\s*field:\s*"([^"]+)"'
    matches = re.findall(pattern, column_defs_regex)

    column_dictionary = {}
    for match in matches:
        column_name = match[0]
        field_name = match[1]
        column_dictionary[field_name] = column_name

    return column_dictionary
