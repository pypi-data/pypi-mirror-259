import logging
import os
from getpass import getpass
from typing import Optional, Tuple

import httpx

from exofop.download.cookie_manager import CookieJarShelf
from exofop.utils.paths import COOKIES_DIR
from exofop.utils.urls import BASE_URL

logger = logging.getLogger(__name__)

# httpx_logger = logging.getLogger("httpx")
# httpx_logger.setLevel(logging.DEBUG)


class ExoFOPAuthenticator:
    """
    A class for managing sessions and login to ExoFOP using httpx.

    Parameters
    ----------
    username : str, optional
        The ExoFOP username. If not provided, user will be prompted to enter.

    Attributes
    ----------
    username : str
        The ExoFOP username used for login.

    Examples
    --------
    >>> authenticator = ExoFOPAuthenticator(username="lovelace")
    Please enter your login credentials:
    Username: myusername  # Username is printed
    Password:             # Password is prompted
    Login was successful. # Or 'Login was not successful'
    """

    BASE_URL = BASE_URL
    """ Base URL for the ExoFOP website. """

    def __init__(
        self,
        username: Optional[str] = None,
        cookies_dir: Optional[str] = None,
        buffer_hours: int = 1,
        credential_file_path: Optional[str] = None,
        number_of_cookie_jars: int = 3,
    ) -> None:
        """
        Initialize the ExoFOPAuthenticator.

        Parameters
        ----------
        username : str, optional
            The ExoFOP username. If not provided, user will be prompted to enter.
        cookies_dir : str, optional
            The directory where the cookies will be stored. If not provided, the default directory
            `exofop.utils.paths.COOKIES_DIR` will be used.
        buffer_hours : int, optional
            The number of hours before the cookies expire, after which new cookies will be requested.
        credential_file_path : str, optional
            The path to a file containing the login credentials.
            The file must be a `.txt` or `.yaml` file.
            The file must contain the username and password in the following format:
            `username: your_username`
            `password: your_password`
            or in a `.txt` file:
            `username=your_username`
            `password=your_password`
        number_of_cookie_jars : int, optional
            The number of cookie jars to use for login. Default is 3.
        """
        self._client = httpx.Client()
        if cookies_dir is None:
            cookies_dir = COOKIES_DIR

        if os.path.exists(cookies_dir) and not os.path.isdir(cookies_dir):
            raise NotADirectoryError(f"{cookies_dir} is not a valid directory.")
        else:
            os.makedirs(cookies_dir, exist_ok=True)

        if credential_file_path is not None:
            username, password = self._read_login_file(credential_file_path)
        else:
            password = None

        if not isinstance(username, str):
            raise TypeError(f"Username must be a string. Got {type(username)} instead.")
        self.username = username
        self.number_of_cookie_jars = number_of_cookie_jars

        cookie_file_path = os.path.abspath(
            os.path.join(cookies_dir, f"exofop_cookies_{self.username}")
        )
        self.cookie_jar_shelf = CookieJarShelf(file_path=cookie_file_path)
        self.cookie_jar_shelf.reduce_number_of_cookie_jars_to(self.number_of_cookie_jars)

        cookies_remain_valid = self.cookie_jar_shelf.cookies_still_valid(buffer_hours=buffer_hours)

        if cookies_remain_valid:
            logger.debug("Cookies were found and are still valid. No need to login.")
            logger.info(f"Cookies will expire in {self.cookie_jar_shelf.get_remaining_validity()}")
        else:
            logger.debug("Cookies were not found, are not valid, or will expire soon. Logging in.")
            if password is not None:
                success = self._login(password=password)

            if not success:
                logger.warning("Login was not successful. Please check your credentials.")

    @property
    def cookies(self):
        """Serve cookies from the cookie_jar_shelf."""
        if not self.cookie_jar_shelf.cookies_still_valid() and not self.login():
            raise ValueError("Login was not successful.")

        return self.cookie_jar_shelf.cookies

    def login(self, password: Optional[str] = None) -> bool:
        """
        Login to ExoFOP and return True if successful.

        Parameters
        ----------
        password : str, optional
            The ExoFOP password. If not provided, user will be prompted to enter.
            For security reasons, it is strongly recommended not to hardcode or directly pass
            your password to this function. Instead, only enter your password when prompted.

        Returns
        -------
        None

        Examples
        --------
        >>> session = ExoFOPAuthenticator(username="lovelace")
        >>> session.login()
        Please enter your login credentials:
        Username: myusername  # Username is printed
        Password:             # Password is prompted
        Login was successful. # Or 'Login was not successful'
        """
        if self.cookie_jar_shelf.cookies_still_valid() and self.number_of_cookie_jars == len(
            self.cookie_jar_shelf
        ):
            logger.info("Cookies are still valid. No need to login.")
            success = True
        else:
            if self.cookie_jar_shelf.cookies_still_valid():
                logger.info(
                    f"{len(self.cookie_jar_shelf)} cookies are still valid,"
                    "but more were requested. Logging in."
                )
            else:
                logger.info("Cookies have expired. Logging in.")
            try:
                success = self._login(password=password)
            except Exception as e:
                logger.error(f"An unexpected error occurred during login: {e}")
                success = False

        return success

    def _login(self, password: Optional[str] = None) -> bool:
        login_url = f"{self.BASE_URL}/tess/login.php?ref=%2Ftess%2F"
        # login_url = f"{self.BASE_URL}/tess/password_check.php"

        success = False
        try:
            if self.username is None or password is None:
                self.username, password = self._prompt_login_data()

            if not password:
                raise ValueError("Password cannot be empty.")

            login_data = self._construct_login_data(self.username, password)

            for _ in range(self.number_of_cookie_jars):
                # Check connection to ExoFOP
                initial_response = self._get_initial_cookies(login_url)
                initial_response.raise_for_status()

                login_response = self._send_login_request(login_data)
                login_response.raise_for_status()

                success = self._check_login_success(login_response)
                if success:
                    self.cookie_jar_shelf.add_cookies_from_client(self._client)

                self._client.close()

        except ValueError as ve:
            logger.error(f"Value error occurred during login data extraction: {ve}")
        except httpx.HTTPError as http_error:
            logger.error(f"HTTP error occurred during login: {http_error}")
        except httpx.RequestError as request_error:
            logger.error(f"Request error occurred during login: {request_error}")
        except Exception as e:
            logger.error(f"An unexpected error occurred during login: {e}")
        finally:
            if "password" in locals():
                del password

        self._client.close()

        return success

    def _check_login_success(self, login_response: httpx.Response) -> bool:
        # Alternatively: look for redirect to tess/index.php
        # if "tess/index.php" in str(login_response.url):
        #     logger.info("Login was successful.")
        #     return True
        # else:
        #     logger.error("Login was not successful. Please check your credentials.")
        #     return False

        if "invalid username or password" in login_response.text.lower():
            logger.error("Login was not successful. Invalid username or password.")
            return False
        else:
            logger.info("Login was successful.")
            return True

    def _prompt_login_data(self) -> Tuple[str, str]:
        print("Please enter your login credentials:")
        if self.username is None:
            username = input("Username: ")
        else:
            username = self.username
            print(f"Username: {username}")
        password = getpass("Password: ")
        return username, password

    def _get_initial_cookies(self, url: str) -> httpx.Response:
        response = self._get_client().get(httpx.URL(url))  # Convert the URL string to httpx URL
        return response

    def _construct_login_data(self, username: str, password: str) -> dict[str, str]:
        login_data = {
            "username": username,
            "password": password,
            "ref": "login_user",
            "ref_page": "/tess/",
        }
        return login_data

    def _send_login_request(self, login_data: dict[str, str]) -> httpx.Response:
        """
        Send a login request to ExoFOP and handle redirects.

        Notes
        -----
        Setting follow_redirects=True ensures that the client automatically follows
        HTTP redirects. In the context of a login request, ExoFOP might use
        redirects as part of the authentication process.

        If follow_redirects is set to False, the client will not automatically
        follow redirects, and the response may not accurately represent the final
        state after the login process, potentially leading to login failures.
        """
        response = self._get_client().post(
            f"{self.BASE_URL}/tess/password_check.php", data=login_data, follow_redirects=True
        )
        return response

    def _get_client(self):
        if self._client.is_closed:
            client = self._client = httpx.Client()
        else:
            client = self._client
        if not isinstance(client, httpx.Client):
            raise TypeError(
                f"Client is not of type httpx.Client. Got {type(self._client)} instead."
            )
        return client

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(username={self.username!r})"

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(username={self.username!s}, "
            f"number_of_cookie_jars={self.number_of_cookie_jars!s}, "
            f"remaining_validity={self.cookie_jar_shelf.get_remaining_validity()!s}"
            ")"
        )

    @staticmethod
    def _read_login_file(credential_file_path: str) -> Tuple[str, str]:
        """Read username and password from a .txt or .yaml file.

        Parameters
        ----------
        credential_file_path : str
            The path to the file containing the login credentials.
            The file must be a .txt or .yaml file.

        """
        username = None
        password = None

        if ".txt" in credential_file_path:
            with open(credential_file_path, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("username="):
                        username = line.split("=")[1].strip()
                    elif line.startswith("password="):
                        password = line.split("=")[1].strip()
        elif credential_file_path.endswith(".yaml"):
            import yaml

            with open(credential_file_path, "r") as f:
                data = yaml.safe_load(f)
                username = data["username"]
                password = data["password"]
        else:
            raise ValueError(
                f"File type of {credential_file_path} not supported."
                "Please provide a .txt or .yaml file, with the following format:\n"
                "username=your_username\n"
                "password=your_password\n"
                "or a .yaml file with the following format:\n"
                "username: your_username\n"
                "password: your_password\n"
            )

        if not isinstance(username, str):
            raise TypeError(f"Username must be a string. Got {type(username)} instead.")
        if not isinstance(password, str):
            raise TypeError(f"Password must be a string. Got {type(password)} instead.")

        return username, password
