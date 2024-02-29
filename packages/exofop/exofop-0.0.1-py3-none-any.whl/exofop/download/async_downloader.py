import asyncio
import os
import logging
from collections import Counter
from enum import Enum
# from http import HTTPStatus
from pathlib import Path
from typing import Iterator, Optional, Union
from urllib.parse import urlsplit

import aiofiles
import aiofiles.os
import httpx
import tqdm.auto as tqdm  # type: ignore

logger = logging.getLogger("exofop.download")
DownloadStatus = Enum("DownloadStatus", "OK NOT_FOUND ERROR TIMEOUT")

class AsyncDownloader:
    """
    Asynchronous file downloader with concurrent download support.

    This class allows asynchronous downloading of files from specified URLs. It supports
    concurrent downloads with customizable parameters such as the maximum number of
    concurrent downloads, timeout, and the ability to display download progress.

    Parameters
    ----------
    async_client : Optional[httpx.AsyncClient], default=None
        Asynchronous HTTP client. If not provided, a new client will be created.
    download_directory : str, default='.'
        Directory to save downloaded files.
    max_concurrent_downloads : int, default=5
        Maximum number of concurrent downloads.
    timeout : float, default=10.0
        Timeout for each download in seconds.
    display_progress : bool, default=True
        Whether to display download progress.

    Methods
    -------
    download_files(url_list, download_directory=None, file_names=None, async_client=None, client_kwargs=None)
        Asynchronously download files from a list of URLs.


    Examples
    --------
    >>> from exofop.download.async_downloader import AsyncDownloader, DownloadStatus
    >>> import os
    >>> download_dir = "."
    >>> downloader = AsyncDownloader(download_directory=download_dir, timeout=100)

    # Create a list of URLs and file names
    >>> file_names = [f"file_{i}.zip" for i in range(4)]
    >>> server_url = "http://localhost:8001/"
    >>> url_list = [os.path.join(server_url, name) for name in file_names]

    # Download files
    >>> counts = downloader.download_files(url_list=url_list, file_names=file_names)
    >>> print(counts)
    Counter({<DownloadStatus.OK: 1>: 2})  # Output might differ, depending on success of download

    # Download files without specifying file names
    >>> dl.download_files(url_list=url_list, max_retries=1)
    Counter({<DownloadStatus.OK: 1>: 2})  # Output might differ, depending on success of download

    Note:
    -----
    Requires the `httpx` library for asynchronous HTTP requests.
    The class is inspired by an example from Luciano Ramalho's excellent book "Fluent Python".
    The original code can be found here:
    https://github.com/fluentpython/example-code-2e/blob/master/20-executors/getflags/flags3_asyncio.py
    """

    def __init__(
        self,
        async_client: Optional[httpx.AsyncClient] = None,
        download_directory: str = ".",
        max_concurrent_downloads: int = 5,
        transport_retries: int = 5,
        timeout: float = 10.0,
        display_progress: bool = True,
        max_retries: int = 1,
        cookie_feeder: Optional[Iterator] = None,
    ):
        self.async_client = async_client or httpx.AsyncClient()

        self.max_concurrent_downloads = max_concurrent_downloads
        self.timeout = timeout
        self.display_progress = display_progress
        self.download_directory = os.path.realpath(download_directory)

        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)

        self.transport = httpx.AsyncHTTPTransport(retries=transport_retries)
        self.max_retries = max_retries
        self.cookie_feeder = cookie_feeder

    def download_files(
        self,
        url_list: list[str],
        download_directory: Optional[str] = None,
        file_names: Optional[list[str]] = None,
        async_client: Optional[httpx.AsyncClient] = None,
        client_kwargs: Optional[dict] = None,
    ) -> Counter[DownloadStatus]:
        counts = asyncio.run(
            self.download_supervisor(
                    url_list=url_list,
                    file_names=file_names,
                    download_directory=download_directory,
                    async_client=async_client,
                    client_kwargs=client_kwargs,
                )
        )

        return counts

    async def download_supervisor(
        self,
        url_list: list[str],
        file_names: Optional[Union[list[str], list[None]]] = None,
        download_directory: Optional[str] = None,
        async_client: Optional[httpx.AsyncClient] = None,
        client_kwargs: Optional[dict] = None,
    ) -> Counter[DownloadStatus]:
        if file_names is None:
            file_names = [None] * len(url_list)
        if client_kwargs is None:
            client_kwargs = {}
        client_kwargs.setdefault("transport", self.transport)

        if async_client is None:
            async_client = httpx.AsyncClient(**client_kwargs)
        if download_directory is None:
            download_directory = self.download_directory

        counter: Counter[DownloadStatus] = Counter()
        semaphore = asyncio.Semaphore(min(self.max_concurrent_downloads, len(url_list)))

        self.validate_async_client(async_client)

        async with async_client as client:
            tasks = [
                # self.download_and_save_file_with_progress(
                self.download_and_save_file_with_retry(
                    client=client,
                    url=url,
                    file_name=file_name,
                    download_directory=download_directory,
                    semaphore=semaphore,
                    timeout=self.timeout,
                    max_retries=self.max_retries,
                )
                for url, file_name in zip(url_list, file_names)
            ]

            task_iterator = asyncio.as_completed(tasks)
            if self.display_progress:
                task_iterator = tqdm.tqdm(
                    task_iterator,
                    total=len(url_list),
                    # position=0,
                    desc="Downloading files.",
                    leave=True,
                    ascii=" >=",
                    bar_format="{l_bar}{bar:10}{r_bar}{bar:-10b}",
                )
            error: httpx.HTTPError | None = None

            for coroutine in task_iterator:
                try:
                    status = await coroutine
                except httpx.HTTPStatusError as exc:
                    error_msg = (
                        f"HTTP error {exc.response.status_code} - {exc.response.reason_phrase}"
                    )
                    logger.debug(error_msg, exc_info=True)
                    error = exc
                except httpx.RequestError as exc:
                    error_msg = f"{exc} {type(exc)}".strip()
                    logger.debug(f"Request error: {error_msg}", exc_info=True)
                    error = exc
                except KeyboardInterrupt:
                    break

                if error:
                    status = DownloadStatus.ERROR

                    url = str(error.request.url)
                    identifier = Path(url).stem.upper()
                    logger.error(f"{identifier} error: {error_msg}")

                counter[status] += 1

            if self.display_progress:
                task_iterator.close()

        return counter

    async def download_and_save_file_with_retry(
        self,
        client: httpx.AsyncClient,
        url: str,
        file_name: Optional[str],
        download_directory: str,
        semaphore: asyncio.Semaphore,
        timeout: float = 10,
        max_retries=0,
        show_progress=True,
    ):
        cookies = None if self.cookie_feeder is None else next(self.cookie_feeder)

        status = DownloadStatus.ERROR

        for retry in range(max_retries + 1):
            try:
                await self.download_file_with_progress(
                    client=client,
                    url=url,
                    file_name=file_name,
                    download_directory=download_directory,
                    semaphore=semaphore,
                    cookies=cookies,
                    timeout=timeout,
                    show_progress=show_progress,
                )
            except httpx.HTTPStatusError as exc:
                logger.error(
                    f"HTTP error {exc.response.status_code} - {exc.response.reason_phrase}",
                )
            except httpx.RequestError as exc:
                logger.error(f"Request error: {exc}")
            except Exception as exc:
                logger.error(f"An unexpected error occurred: {exc}", exc_info=True)
                break
            else:
                status = DownloadStatus.OK

            # Exit the loop if the download is successful
            if status == DownloadStatus.OK:
                break

            if retry < max_retries:
                logger.warning(f"Retrying download ({retry + 1}/{max_retries + 1}) for {url}")
                await asyncio.sleep(2**retry)
            elif retry == max_retries and status != DownloadStatus.OK:
                status = DownloadStatus.TIMEOUT

        # try:
        #     await self.download_and_save_file_with_progress(
        #         client=client,
        #         url=url,
        #         file_name=file_name,
        #         download_directory=download_directory,
        #         semaphore=semaphore,
        #         timeout=timeout,
        #         max_retries=max_retries,
        #         show_progress=show_progress,
        #     )
        # except httpx.HTTPStatusError as exc:
        #     logger.error(
        #         f"HTTP error {exc.response.status_code} - {exc.response.reason_phrase}",
        #     )
        # except httpx.RequestError as exc:
        #     logger.error(f"Request error: {exc}")
        # except Exception as exc:
        #     logger.error(f"An unexpected error occurred: {exc}", exc_info=True)
        # else:
        #     status = DownloadStatus.OK

        logger.info(f"{file_name=}: {status.name}")

        return status

    @staticmethod
    async def download_file_with_progress(
        client: httpx.AsyncClient,
        url: str,
        file_name: Optional[str],
        download_directory: str,
        semaphore: asyncio.Semaphore,
        cookies=None,
        timeout: float = 10,
        show_progress=True,
    ):
        async with semaphore, client.stream("GET", url, timeout=timeout, cookies=cookies) as response:
                response.raise_for_status()
                file_name = AsyncDownloader.extract_filename_from_url_or_headers(
                    url, response, file_name
                )
                total = int(response.headers["Content-Length"])
                file_path = os.path.join(download_directory, file_name)

                try:
                    async with aiofiles.open(file_path, "wb") as download_file:
                        with tqdm.tqdm(
                            total=total,
                            unit_scale=True,
                            unit_divisor=1024,
                            unit="B",
                            desc=f"Downloading {os.path.basename(file_name)}",
                            leave=True,
                            bar_format="{l_bar}{bar:10}{r_bar}{bar:-10b}",
                            disable=not show_progress,
                        ) as progress:
                            num_bytes_downloaded = response.num_bytes_downloaded
                            async for chunk in response.aiter_bytes():
                                await download_file.write(chunk)
                                progress.update(response.num_bytes_downloaded - num_bytes_downloaded)
                                num_bytes_downloaded = response.num_bytes_downloaded
                except Exception as exc:
                    # Remove empty files
                    if await aiofiles.os.path.getsize(file_path) == 0:
                        logger.debug(f"Removing empty file {file_path}")
                        await aiofiles.os.remove(file_path)
                    raise exc

    @staticmethod
    def extract_filename_from_url_or_headers(
        url: str, response: httpx.Response, file_name: str
    ) -> str:
        # Extract filename from the URL or response headers
        url_path = urlsplit(url).path
        filename = (
            file_name
            or os.path.basename(url_path)
            or response.headers.get("content-disposition", "").split("filename=")[1].strip('"')
        )
        return filename

    @staticmethod
    def validate_async_client(async_client):
        if not isinstance(async_client, httpx.AsyncClient):
            raise TypeError(
                f"async_client is not of type httpx.AsyncClient. Got {type(async_client)} instead."
            )
        elif async_client.is_closed:
            raise ValueError("async_client is closed.")

    async def close_async_client(self):
        await self.async_client.aclose()

    def __repr__(self):
        return (
            f"AsyncDownloader("
            f"async_client={self.async_client}, "
            f"download_directory='{self.download_directory}', "
            f"max_concurrent_downloads={self.max_concurrent_downloads}, "
            f"timeout={self.timeout}, "
            f"show_progress={self.display_progress})"
        )
