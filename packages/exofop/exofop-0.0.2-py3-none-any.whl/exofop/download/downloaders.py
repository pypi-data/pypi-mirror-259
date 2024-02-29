import logging
import os
import shutil
import time
import zipfile
from collections import Counter
from functools import cache
from io import StringIO
from typing import Optional, Union
import asyncio

import astropy
import astropy.table
import httpx
import numpy as np

from exofop.download.authenticator import ExoFOPAuthenticator
from exofop.download.async_downloader import AsyncDownloader, DownloadStatus
from exofop.download.identifiers import TIC, TOI, System
from exofop.utils.urls import BASE_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def is_event_loop_running():
    try:
        loop = asyncio.get_event_loop()
        return loop.is_running()
    except RuntimeError:
        return False


class TagDownloader:
    """
    TagDownloader is a class for downloading files associated with a list of ExoFOP tags.

    Parameters
    ----------
    target_dir : str, optional
        The target directory where downloaded and extracted files will be stored.
        Default is the current directory.
    authenticator : exofop.download.authenticator.ExoFOPAuthenticator, optional
        An instance of ExoFOPAuthenticator for authentication to ExoFOP. Default is None.
    downloader : AsyncDownloader, optional
        An instance of AsyncDownloader for handling asynchronous file downloads. Default is None.
    max_concurrent_downloads : int, optional
        The maximum number of concurrent downloads. Default is 5.
    timeout : int, optional
        Timeout in seconds for each download. Default is 100.


    Examples
    --------
    >>> data_dir = '/path/to/data'
    >>> os.makedirs(data_dir, exist_ok=True)
    >>> tdl = TagDownloader(target_dir=data_dir)
    >>> tdl.download_tags(tags=['5903'])
    >>> tdl.unzip_downloaded_files()

    Examples
    --------
    >>> data_dir='/path/to/data'
    >>> authenticator = ExoFOPAuthenticator(username="lovelace")
    >>> os.makedirs(data_dir, exist_ok=True)
    >>> tdl = TagDownloader(target_dir=data_dir, authenticator=authenticator)
    >>> tdl.download_tags(tags=['5734', '5903'])
    >>> tdl.unzip_downloaded_files()

    Notes
    -----
    After downloading the tags 5734 and 5904, the directory structure looks as follows:

    .. highlight:: bash
    .. code-block:: bash

        target_dir/
        ├── 5734/
        ├── 5903/
        ├── zip/
        │   ├── 5734.zip
        │   ├── 5903.zip


    For more information on the ExoFOP API see:
    https://exofop.ipac.caltech.edu/tess/Introduction_to_ExoFOP_php_functions.php

    """

    BASE_URL = BASE_URL

    def __init__(
        self,
        target_dir: str = ".",
        authenticator: Optional[ExoFOPAuthenticator] = None,
        downloader: Optional[AsyncDownloader] = None,
        max_concurrent_downloads=2,
        timeout=5,
        max_retries=1,
    ) -> None:
        self.target_dir = target_dir
        self.zip_dir = os.path.join(self.target_dir, "zip")
        if not os.path.isdir(self.target_dir):
            raise ValueError(f"Data directory does not exist: {self.target_dir}")

        # Provide an ExoFOPAuthenticator object if you want to login to ExoFOP
        if authenticator is not None:
            self.authenticator = authenticator
        else:
            self.authenticator = None

        # Initialise downloader
        if downloader is not None:
            self.downloader = downloader
        else:
            self.downloader = AsyncDownloader(
                download_directory=self.zip_dir,
                max_concurrent_downloads=max_concurrent_downloads,
                timeout=timeout,
                max_retries=max_retries,
            )

        if self.authenticator is not None:
            self.downloader.cookie_feeder = self.authenticator.cookie_jar_shelf.iterator

    @property
    def client_kwargs(self) -> dict:
        """Return the client kwargs for the downloader. 
        
        This includes a set of cookies if an authenticator is provided.
        """
        client_kwargs = {}
        if self.authenticator is not None:
            client_kwargs["cookies"] = self.authenticator.cookies
            logger.debug(
                "client_kwargs: ",
                str(client_kwargs["cookies"]._cookies["exofop.ipac.caltech.edu"]["/"]["PHPSESSID"]),
            )
        return client_kwargs

    # @timing
    def download_tags(
        self,
        tags: Union[np.ndarray, list, str, int],
        download_directory: Optional[str] = None,
    ) -> Counter[DownloadStatus]:
        if download_directory is not None:
            os.makedirs(download_directory, exist_ok=True)

        if isinstance(tags, (str, int)):
            tags = [str(tags)]
        elif not isinstance(tags, (np.ndarray, list)):
            raise TypeError(f"Tags must be of type np.ndarray or list. Got {type(tags)} instead.")

        file_names = [f"{tag}.zip" for tag in tags]
        url_list = [f"{self.BASE_URL}/tess/download_tag_files_zip.php?tag={tag}" for tag in tags]

        counts = self.downloader.download_files(
            url_list=url_list,
            file_names=file_names,
            download_directory=download_directory,  # defaults to self.zip_dir
            client_kwargs=self.client_kwargs,
        )

        self._log_download_success_summary(counts)

        return counts

    async def download_tags_async(
        self,
        tags: Union[np.ndarray, list, str, int],
        download_directory: Optional[str] = None,
    ) -> Counter[DownloadStatus]:
        if download_directory is not None:
            os.makedirs(download_directory, exist_ok=True)

        if isinstance(tags, (str, int)):
            tags = [str(tags)]
        elif not isinstance(tags, (np.ndarray, list)):
            raise TypeError(f"Tags must be of type np.ndarray or list. Got {type(tags)} instead.")

        file_names = [f"{tag}.zip" for tag in tags]
        url_list = [f"{self.BASE_URL}/tess/download_tag_files_zip.php?tag={tag}" for tag in tags]

        counts = await self.downloader.download_supervisor(
            url_list=url_list,
            file_names=file_names,
            download_directory=download_directory,  # defaults to self.zip_dir
            client_kwargs=self.client_kwargs,
        )

        self._log_download_success_summary(counts)

        return counts

    def unzip_downloaded_files(self, output_dir: Optional[str] = None) -> None:
        """
        Unzip all .zip files in the given folder and move the extracted contents to the output path.

        Parameters
        ----------
        output_dir : Optional, str
            The path to the folder where the extracted contents should be moved.

        Examples
        --------
        >>> downloader.unzip_downloaded_files()
        """
        if output_dir is None:
            output_dir = self.target_dir
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        for item in os.listdir(self.zip_dir):
            item_path = os.path.join(self.zip_dir, item)
            if item.endswith(".zip") and os.path.isfile(item_path):
                output_folder_name = os.path.splitext(item)[0]  # name without ".zip" suffix
                try:
                    self._unzip_and_move(item_path, output_dir, output_folder_name)
                except zipfile.BadZipFile as e:
                    logger.error(f"A BadZipFile error occurred while unzipping {item_path}: {e}")
                except Exception as e:
                    logger.error(f"An error occurred while unzipping {item_path}: {e}")

    def _unzip_and_move(self, item_path: str, output_dir: str, output_folder_name: str) -> None:
        """Unzip a .zip file and move the extracted contents to the output path."""
        with zipfile.ZipFile(item_path, "r") as zip_ref:
            # Extract the zip file contents to a temporary folder
            temp_extract_path = os.path.join(self.zip_dir, "temp_extract")
            zip_ref.extractall(temp_extract_path)

            # Get the name of the extracted folder (there should be only one)
            extracted_folder_name = os.listdir(temp_extract_path)[0]

            # Rename the extracted folder to match the zip file's name
            extracted_zip_dir = os.path.join(temp_extract_path, extracted_folder_name)
            new_zip_dir = os.path.join(output_dir, output_folder_name)
            os.makedirs(new_zip_dir, exist_ok=True)

            try:
                os.rename(extracted_zip_dir, new_zip_dir)
                os.rmdir(temp_extract_path)
            except OSError as e:
                if e.errno == 66:
                    logger.error("The directory or file already exists at the target location.")
                else:
                    logger.error(f"An OSError occurred with error code {e.errno}: {e}")
                if os.path.exists(temp_extract_path):
                    shutil.rmtree(temp_extract_path)

    @staticmethod
    def _log_download_success_summary(counts: Counter[DownloadStatus]) -> None:
        for status, count in counts.items():
            logger.debug(f"{count} files with status {status}")

        status_response = counts[DownloadStatus.OK]
        total_responses = sum(counts.values())
        total_responses = total_responses if total_responses > 0 else 1 # avoid division by zero
        status_rate = round(status_response / total_responses * 100, 2)
        logger.info(
            f"Downloaded {status_response} of {total_responses} files "
            f"({status_rate} %) successfully."
        )

    def delete_zip_folder(self) -> None:
        """
        Delete the .zip folder and all files inside it.

        Examples
        --------
        >>> tag_downloader.delete_zip_folder()
        """
        try:
            shutil.rmtree(self.zip_dir)
            logger.info(f"Deleted {self.zip_dir} and all its contents.")
        except FileNotFoundError:
            logger.warning(f"{self.zip_dir} does not exist. Nothing to delete.")
        except Exception as e:
            logger.error(f"An error occurred while deleting {self.zip_dir}: {e}")

    def __repr__(self) -> str:
        return (
            "TagDownloader("
            f"target_dir={self.target_dir}, "
            f"authenticator={self.authenticator}, "
            f"max_concurrent_downloads={self.downloader.max_concurrent_downloads}, "
            f"timeout={self.downloader.timeout}"
            ")"
        )


class ExofopTable:
    BASE_URL = BASE_URL
    TERM = "target"
    RESOURCE = "download_tseries.php"
    DEFAULT_FILE_NAME = "exofop_table"

    def __init__(
        self,
        target_dir: str = ".",
    ) -> None:
        self.target_dir = os.path.realpath(target_dir)
        if not os.path.isdir(self.target_dir):
            raise ValueError(f"Data directory does not exist: {self.target_dir}")

    def get_url(self, term: str):
        return f"{self.BASE_URL}/tess/{self.RESOURCE}?{self.TERM}={term}&output=pipe"

    @staticmethod
    def preprocess_term(
        term: Optional[Union[int, str]] = None,
        system_name: Optional[str] = None,
        toi: Optional[str] = None,
        tic: Optional[Union[int, str]] = None,
    ) -> str:
        if term is None:
            term = System(name=system_name, toi=toi, tic=tic).target
        elif isinstance(term, int):
            term = str(term)
        return term

    def download(
        self,
        system_name: Optional[str] = None,
        toi: Optional[str] = None,
        tic: Optional[Union[int, str]] = None,
        target: Optional[Union[int, str]] = None,
        target_dir: Optional[str] = None,
        file_name: Optional[str] = None,
        save: bool = True,
    ) -> astropy.table.Table:
        term = self.preprocess_term(term=target, system_name=system_name, tic=tic, toi=toi)
        return self._download(term=term, target_dir=target_dir, file_name=file_name, save=save)

    @cache
    def _download(
        self,
        term: Optional[str] = None,
        target_dir: Optional[str] = None,
        file_name: Optional[str] = None,
        save: bool = True,
    ) -> astropy.table.Table:
        """Download time series observations table for a given system name, target, TIC ID, or TOI ID.

        Returns
        -------
        tab : astropy.table.Table
            Table containing the time series observations table. Returns None if an error occurs.
        """
        # target=[nnnnnnnnn|TOInnn]
        url = self.get_url(str(term))
        tab = self._download_csv_from_url(url)

        if target_dir is None:
            target_dir = self.target_dir

        if save:
            if file_name is None:
                file_name = f"{self.DEFAULT_FILE_NAME}_{term}.csv"

            file_name = os.path.join(target_dir, file_name)
            tab.write(file_name, format="ascii.csv", overwrite=True)

        return tab

    def _download_csv_from_url(self, url: str) -> astropy.table.Table:
        try:
            # This seems slightly faster than converting to io.StringIO and then to Table
            tab = astropy.table.Table.read(url, delimiter="|", format="ascii.csv", header_start=0)
        except Exception:
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()

            try:
                tab = astropy.table.Table.read(
                    StringIO(response.text), delimiter="|", format="ascii.csv", header_start=0
                )
            except Exception as e:
                raise ValueError(
                    f"An error occurred while processing the pipe file. Original exception: {e}"
                ) from e
        # return df
        return tab

    def bulk_download(
        self,
        system_names: Optional[list[str]] = None,
        target_list: Optional[list[str]] = None,
        tic_list: Optional[list[Union[str, int]]] = None,
        toi_list: Optional[list[Union[str, int]]] = None,
        file_names: Optional[list[str]] = None,
        target_dir: Optional[str] = None,
        to_separate_folders: bool = False,
        downloader: Optional[AsyncDownloader] = None,
        client_kwargs: Optional[dict] = None,
        max_concurrent_downloads: int = 5,
        timeout: float = 100,
    ) -> Counter[DownloadStatus]:
        """
        Download multiple time series observations tables for a list of TIC IDs or TOI IDs.

        Example
        -------
        >>> toi_list = ['TOI_1130', 'TOI_1131']
        >>> dl.TimeSeriesTable.bulk_download(toi_list=toi_list, to_separate_folders=False)
        """
        if target_dir is None:
            target_dir = self.target_dir

        # Prepare target list of valid target names for the php query, i.e. TIC IDs or TOI IDs
        if target_list is None:
            target_list = self._prepare_target_list(tic_list, toi_list)

        if downloader is None:
            downloader = AsyncDownloader(
                download_directory=target_dir,
                max_concurrent_downloads=max_concurrent_downloads,
                timeout=timeout,
            )

        if client_kwargs is None:
            client_kwargs = {}

        if file_names is None:
            file_names = self._prepare_file_names(
                file_names=file_names,
                system_names=system_names,
                to_separate_folders=to_separate_folders,
                target_list=target_list,
                target_dir=target_dir,
            )

        url_list = [self.get_url(target) for target in target_list]

        # Execute download
        counts = downloader.download_files(
            url_list=url_list,
            file_names=file_names,
            download_directory=target_dir,
            client_kwargs=client_kwargs,
        )
        return counts

    @staticmethod
    def _prepare_target_list(tic_list, toi_list):
        if not (isinstance(tic_list, list) or isinstance(toi_list, list)):
            raise ValueError("Either `tic_list` or `toi_list` must be provided.")

        if tic_list is not None:
            target_list = [TIC(tic).id for tic in tic_list]
        elif toi_list is not None:
            target_list = [TOI(toi).id for toi in toi_list]
        else:
            raise ValueError("Either `tic_list` or `toi_list` must be provided.")

        return target_list

    @staticmethod
    def _prepare_file_names(file_names, system_names, to_separate_folders, target_list, target_dir):
        if system_names is None:
            system_names = target_list
        if to_separate_folders:
            file_names = [
                os.path.join(system_name, f"time_series_observations_{system_name}.csv")
                for system_name in system_names
            ]
            folders = [os.path.join(target_dir, system_name) for system_name in system_names]
            for system_dir in folders:
                os.makedirs(system_dir, exist_ok=True)
        else:
            file_names = [
                f"time_series_observations_{system_name}.csv" for system_name in system_names
            ]
        return file_names

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(" f"target_dir={self.target_dir})"


class ExofopIDTable(ExofopTable):
    # Ensure that all targets are TIC IDs, not TOI IDs
    TERM = "id"

    @staticmethod
    def preprocess_term(
        term: Optional[Union[int, str]] = None,
        system_name: Optional[str] = None,
        toi: Optional[str] = None,
        tic: Optional[Union[int, str]] = None,
    ) -> str:
        if term is None:
            term = System(name=system_name, toi=toi, tic=tic).get_tic().id
        elif isinstance(term, int):
            term = str(term)
        return term

    @staticmethod
    def _prepare_target_list(tic_list, toi_list):
        if not (isinstance(tic_list, list) or isinstance(toi_list, list)):
            raise ValueError("Either `tic_list` or `toi_list` must be provided.")

        if tic_list is not None:
            target_list = [TIC(tic).id for tic in tic_list]
        elif toi_list is not None:
            target_list = [TOI(toi).to_tic().id for toi in toi_list]
        else:
            raise ValueError("Either `tic_list` or `toi_list` must be provided.")

        return target_list


class TimeSeriesTable(ExofopTable):
    """
    Class for downloading time series observations tables.

    This class provides methods to download time series observations tables from the ExoFOP database.
    These tables are contained in the "Time Series Observations" section of a given target's
    ExoFOP page. They contain the following columns:
    'TIC ID', 'TIC', 'TOI', 'Telescope', 'Camera', 'Filter', 'Pixel Scale', 'PSF',
    'Phot Aperture Rad', 'Obs Date', 'Obs Duration', 'Num Obs', 'Obs Type', 'Transit Coverage',
    'Delta Mag', 'User', 'Group', 'Tag', 'Notes'.


    Parameters
    ----------
    target_dir : str, optional
        The target directory for storing downloaded files. Defaults to the current directory.

    Attributes (Constants)
    -----------------------
    BASE_URL : str
        Base URL for downloading time series observations tables.

    Methods
    -------
    download(
        system_name: Optional[str] = None,
        toi: Optional[str] = None,
        tic: Optional[Union[int, str]] = None,
        target: Optional[Union[int, str]] = None,
        target_dir: Optional[str] = None
    ) -> astropy.table.Table
        Download time series observations table for a given system name, TIC ID, or TOI ID.
        Note that only one of `system_name`, `toi`, `tic`, or `target` need to be provided.
        If `system_name` is used, the system's TIC ID will be looked up.

    bulk_download(
        system_names: Optional[list[str]] = None,
        target_list: Optional[list[str]] = None,
        tic_list: Optional[list[Union[str, int]]] = None,
        toi_list: Optional[list[Union[str, int]]] = None,
        file_names: Optional[list[str]] = None,
        target_dir: Optional[str] = None,
        to_separate_folders: bool = False,
        downloader: Optional[AsyncDownloader] = None,
        client_kwargs: Optional[dict] = None,
        max_concurrent_downloads: int = 5,
        timeout: float = 100,
    ) -> Counter[DownloadStatus]
        Download time series observations table for a list of TIC IDs or TOI IDs.
        Note that only one of `target_list`, `tic_list`, or `toi_list` need to be provided.
        Lazy inference of TIC ID or TOI ID using `system_names` is not implemented for this method.

    Examples
    --------
    >>> table = TimeSeriesTable(target_dir=data_dir)
    >>> df = table.download(toi='TOI_1130')  # == table.download(target=TOI('TOI_1130').id)

    >>> toi_list = ['TOI_1130', 'TOI_1131']
    >>> table.bulk_download(toi_list=toi_list, to_separate_folders=False)
    """
    DEFAULT_FILE_NAME = "time_series_observations_overview"
    RESOURCE = "download_tseries.php"


class SpectroscopyTable(ExofopTable):
    """
    >>> table = SpectroscopyTable(target_dir=data_dir)
    >>> df = table.download(toi='TOI_1130')
    """
    DEFAULT_FILE_NAME = "spectroscopy_observations_overview"
    RESOURCE = "download_spect.php"


class ImagingTable(ExofopTable):
    """
    >>> imaging_table = ImagingTable(target_dir=data_dir)
    >>> df = imaging_table.download(toi='TOI_1130')
    """
    DEFAULT_FILE_NAME = "imaging_observations_overview"
    RESOURCE = "download_imaging.php"


class StellarParametersTable(ExofopIDTable):
    """
    tb = StellarParametersTable(target_dir=data_dir)
    tb.download(toi='TOI_1130')
    """
    DEFAULT_FILE_NAME = "stellar_parameters_overview"
    RESOURCE = "download_stellar.php"


class NearbyTargetTable(ExofopIDTable):
    """
    tb = NearbyTargetTable(target_dir=data_dir)
    tb.download(toi='TOI_1130')
    """
    DEFAULT_FILE_NAME = "nearby_target_overview"
    RESOURCE = "download_nearbytarget.php"


class StellarCompanionsTable(ExofopTable):
    """
    tb = StellarCompanionsTable(target_dir=data_dir)
    tb.download(toi='TOI_1130')
    """
    DEFAULT_FILE_NAME = "stellar_companions_overview"
    RESOURCE = "download_stellarcomp.php"


class OverviewTableAccessor:
    """A class for providing tables from ExoFOP for a given target."""

    def __init__(self, table_loader: ExofopTable, target: str, target_dir: str = ".") -> None:
        self.target = target
        self.target_dir = target_dir
        self.table_loader = table_loader
        self._table = None

    @property
    def table(self) -> astropy.table.Table:
        """The table containing the data for the given target."""
        if self._table is None:
            self._table = self._download()
        return self._table

    @property
    def tags(self) -> np.ndarray:
        """The list of tags contained in the table for the given target."""
        if self._table is None:
            self._table = self._download()

        if isinstance(self._table["Tag"].data, np.ma.MaskedArray):
            return self._table["Tag"].compressed()
        else:
            return self._table["Tag"].data

    def _download(self) -> astropy.table.Table:
        """Download the table for the given target."""
        return self.table_loader.download(target=self.target, target_dir=self.target_dir)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(" f"target={self.target}, table_loader={self.table_loader})"
        )


class SystemDownloader(TagDownloader):
    """
    A class for downloading data related to individual stellar systems from ExoFOP.

    Parameters
    ----------
    system : exofop.download.identifiers.System
        The system identifier for the given system.
    data_dir : str, optional
        The directory where downloaded and extracted files will be stored. Default is the current directory.
    target_dir : str, optional
        The target directory where downloaded and extracted files will be stored. Default is None.
    add_exofop_subdir : bool, optional
        Whether to add a subdirectory for ExoFOP data. Default is False.
    authenticator : exofop.download.authenticator.ExoFOPAuthenticator, optional
        An instance of ExoFOPAuthenticator for authentication to ExoFOP. Default is None.
    downloader : AsyncDownloader, optional
        An instance of AsyncDownloader for handling asynchronous file downloads. Default is None.
    max_concurrent_downloads : int, optional
        The maximum number of concurrent downloads. Default is 2.
    timeout : int, optional
        Timeout in seconds for each download. Default is 5.
    max_retries : int, optional
        The maximum number of retries for each download. Default is 1.

    Attributes
    ----------
    time_series : OverviewTableAccessor
        The time series table for the given system.
    spectroscopy : OverviewTableAccessor
        The spectroscopy table for the given system.
    imaging : OverviewTableAccessor
        The imaging table for the given system.
    stellar_parameters : OverviewTableAccessor
        The stellar parameters table for the given system.
    nearby_target : OverviewTableAccessor
        The nearby target table for the given system.
    stellar_companions : OverviewTableAccessor
        The stellar companions table for the given system.

    Examples
    --------
    >>> system_loader = SystemDownloader(
    ...     data_dir=data_dir,
    ...     system=System('TIC_254113311'),
    ...     max_retries=0
    ... )

    Lets say we want to download the time series observations.
    We will first see what observations are available:

    >>> tab = system_loader.time_series.table

    Then we can download the tags that we are interested in:

    >>> tags = system_loader.time_series.tags
    >>> system_loader.download(tags[[1, 3]])

    To download all time series data for a given system:

    >>> system_loader.download_time_series()

    """

    def __init__(
        self,
        system: System,
        data_dir: str = ".",
        target_dir=None,
        add_exofop_subdir: bool = False,
        authenticator: Optional[ExoFOPAuthenticator] = None,
        downloader: Optional[AsyncDownloader] = None,
        max_concurrent_downloads=2,
        timeout=5,
        max_retries=1,
    ) -> None:
        self.system = system

        if target_dir is None:
            target_dir = os.path.join(data_dir, str(self.system.name))
        if add_exofop_subdir:
            target_dir = os.path.join(target_dir, "exofop")

        os.makedirs(target_dir, exist_ok=True)

        self.time_series = OverviewTableAccessor(
            table_loader=TimeSeriesTable(), target=self.system.target, target_dir=target_dir
        )
        self.spectroscopy = OverviewTableAccessor(
            table_loader=SpectroscopyTable(), target=self.system.target, target_dir=target_dir
        )
        self.imaging = OverviewTableAccessor(
            table_loader=ImagingTable(), target=self.system.target, target_dir=target_dir
        )
        self.stellar_parameters = OverviewTableAccessor(
            table_loader=StellarParametersTable(),
            target=self.system.get_tic().id,
            target_dir=target_dir,
        )
        self.nearby_target = OverviewTableAccessor(
            table_loader=NearbyTargetTable(), target=self.system.target, target_dir=target_dir
        )
        self.stellar_companions = OverviewTableAccessor(
            table_loader=StellarCompanionsTable(), target=self.system.target, target_dir=target_dir
        )

        super().__init__(
            target_dir=target_dir,
            authenticator=authenticator,
            downloader=downloader,
            max_concurrent_downloads=max_concurrent_downloads,
            timeout=timeout,
            max_retries=max_retries,
        )

    @property
    def light_curve(self):
        """The light curve table for the given system. Alternative name for `time_series`.

        See Also
        --------
        time_series : OverviewTableAccessor
            The light curve table for the given system.
        """
        return self.time_series

    def download(self, tags, output_dir: Optional[str] = None, unzip=True):
        """Download all all files specified by the given tags.

        Parameters
        ----------
        tags : list[str]
            The list of tags for the files to be downloaded.
        output_dir : Optional[str]
            The directory where the downloaded files should be stored. Default is None.
        unzip : bool
            Whether to unzip the downloaded files. Default is True.

        Returns
        -------
        counts : Counter[DownloadStatus]
            A Counter object containing the number of files with each download status.
        """
        if output_dir is None:
            output_dir = self.target_dir

        if is_event_loop_running():
            return self._download_async(tags=tags, output_dir=output_dir, unzip=unzip)

        start_time = time.perf_counter()
        counts = self.download_tags(tags=tags)
        end_time = time.perf_counter()

        self._log_download_summary(start_time, end_time, counts)

        if unzip:
            self.unzip_downloaded_files(output_dir=self.target_dir)

        return counts

    async def _download_async(self, tags, output_dir: str, unzip=True):
        """Asynchronous version of the download method.

        This method is used if an event loop is already running, as is the case in Jupyter notebooks.

        See Also
        --------
        download : Method for downloading files asynchronously.
        """
        start_time = time.perf_counter()
        counts = await self.download_tags_async(tags=tags)
        end_time = time.perf_counter()

        self._log_download_summary(start_time, end_time, counts)

        if unzip:
            self.unzip_downloaded_files(output_dir=self.target_dir)

    @staticmethod
    def _log_download_summary(start_time, end_time, counts: Counter[DownloadStatus]) -> None:
        logger.info(
            f"Successfully downloaded {counts[DownloadStatus.OK]} files in {end_time - start_time} seconds."
        )

    def download_time_series(
        self,
        output_dir: Optional[str] = None,
        unzip: bool = True,
    ) -> Counter[DownloadStatus]:
        """Download all time series observations tables for the given system.

        Convenience method for downloading all time series observations tables for the given system,
        and optionally unzipping the downloaded files.

        Parameters
        ----------
        output_dir : Optional[str]
            The directory where the downloaded files should be stored. Default is None.
        unzip : bool
            Whether to unzip the downloaded files. Default is True.
        """
        tags = self.time_series.tags
        if output_dir is None:
            output_dir = os.path.join(self.target_dir, "time_series")
        return self.download(tags=tags, output_dir=output_dir, unzip=unzip)

    def download_spectroscopy(
        self,
        output_dir: Optional[str] = None,
        unzip: bool = True,
    ) -> Counter[DownloadStatus]:
        """Download all spectroscopy tables for the given system.

        Convenience method for downloading all spectroscopy tables for the given system,
        and optionally unzipping the downloaded files.

        Parameters
        ----------
        output_dir : Optional[str]
            The directory where the downloaded files should be stored. Default is None.
        unzip : bool
            Whether to unzip the downloaded files. Default is True.
        """
        tags = self.time_series.tags
        if output_dir is None:
            output_dir = os.path.join(self.target_dir, "spectroscopy")
        return self.download(tags=tags, output_dir=output_dir, unzip=unzip)

    def download_imaging(
        self,
        output_dir: Optional[str] = None,
        unzip: bool = True,
    ) -> Counter[DownloadStatus]:
        """Download all imaging tables for the given system.

        Convenience method for downloading all imaging tables for the given system,
        and optionally unzipping the downloaded files.

        Parameters
        ----------
        output_dir : Optional[str]
            The directory where the downloaded files should be stored. Default is None.
        unzip : bool
            Whether to unzip the downloaded files. Default is True.
        """
        tags = self.time_series.tags
        if output_dir is None:
            output_dir = os.path.join(self.target_dir, "imaging")
        return self.download(tags=tags, output_dir=output_dir, unzip=unzip)

    def unzip_downloaded_files(self, output_dir: Optional[str] = None) -> None:
        """Unzip all downloaded files for the given system.

        Unzip all downloaded files for the given system and move the extracted contents to the output path.

        Parameters
        ----------
        output_dir : Optional[str]
            The path to the folder where the extracted contents should be moved. Default is None.
        """
        if output_dir is None:
            output_dir = self.target_dir

        super().unzip_downloaded_files(output_dir=output_dir)

    def __repr__(self) -> str:
        return (
            super().__repr__()[:-1]
            + f", system={self.system}, add_exofop_subdir={self.target_dir.endswith('exofop')})"
        )

    @classmethod
    def from_username(
        cls,
        username: str,
        system: System,
        data_dir: str = ".",
        target_dir=None,
        add_exofop_subdir: bool = False,
        downloader: Optional[AsyncDownloader] = None,
        max_concurrent_downloads=5,
        timeout=100,
    ):
        authenticator = ExoFOPAuthenticator(username=username)

        return cls(
            system=system,
            data_dir=data_dir,
            target_dir=target_dir,
            add_exofop_subdir=add_exofop_subdir,
            authenticator=authenticator,
            downloader=downloader,
            max_concurrent_downloads=max_concurrent_downloads,
            timeout=timeout,
        )
