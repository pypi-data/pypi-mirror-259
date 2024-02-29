import datetime
import http.cookiejar
import logging
import os
from itertools import cycle

import yaml

logger = logging.getLogger(__name__)


class CookieJarShelf:
    def __init__(self, cookie_jar_shelf=None, file_path="./cookies"):
        if cookie_jar_shelf is None:
            cookie_jar_shelf = []
        self.cookie_jar_shelf: list[http.cookiejar.CookieJar] = cookie_jar_shelf

        self.file_path = file_path
        if not self.cookie_jar_shelf:
            self.load_from_file()

        self.remove_expired_cookies()

        # sorted(
        #     self.cookie_jar_shelf,
        #     key=lambda cookie_jar: self.get_remaining_validity_cookie_jar(cookie_jar) or -10,
        # )

        self.iterator = cycle(self.cookie_jar_shelf)

    @property
    def cookies(self):
        if not self.cookie_jar_shelf:
            raise ValueError("No cookies found. Please log in first.")
        if not self.cookies_still_valid():
            raise ValueError("Cookies have expired. Please log in again.")

        cookie_jar = next(self.iterator)
        if not isinstance(cookie_jar, http.cookiejar.CookieJar):
            raise TypeError(
                f"Cookie jar is not of type http.cookiejar.CookieJar. Got {type(cookie_jar)} instead."
            )

        return cookie_jar

    def add_cookies_from_client(self, client):
        self.cookie_jar_shelf.append(client.cookies.jar)
        self.save_to_file()

    def save_to_file(self) -> None:
        for i, cookie_jar in enumerate(self.cookie_jar_shelf):
            mozilla_cookie_jar = http.cookiejar.MozillaCookieJar()

            for cookie in cookie_jar:
                mozilla_cookie_jar.set_cookie(cookie)

            mozilla_cookie_jar.save(self.file_path + f"_{i}.txt", ignore_discard=True)

        def cookie_representer(dumper, data):
            return dumper.represent_mapping("!http.cookiejar.Cookie", data.__dict__)

        yaml.add_representer(http.cookiejar.Cookie, cookie_representer)

        with open(self.file_path + ".yaml", "w") as yaml_file:
            yaml.dump(
                [cookie_jar._cookies for cookie_jar in self.cookie_jar_shelf],
                yaml_file,
                default_flow_style=False,
            )  # type: ignore

    def load_from_file(self) -> bool:
        def cookie_constructor(
            loader: yaml.SafeLoader, node: yaml.nodes.MappingNode
        ) -> http.cookiejar.Cookie:
            value = loader.construct_mapping(node, deep=True)
            value["rest"] = value.pop("_rest", None)
            return http.cookiejar.Cookie(**value)  # type: ignore

        if not os.path.exists(self.file_path + ".yaml"):
            return False

        yaml.SafeLoader.add_constructor("!http.cookiejar.Cookie", cookie_constructor)

        with open(self.file_path + ".yaml", "r") as file:
            saved_shelf = yaml.safe_load(file)

        self.cookie_jar_shelf = [http.cookiejar.CookieJar() for _ in saved_shelf]

        for cookie_jar, cookie_dict in zip(self.cookie_jar_shelf, saved_shelf):
            cookie_jar._cookies = cookie_dict

        if self.cookies_still_valid():
            return True

        return False

    def cookies_still_valid(self, buffer_hours=0) -> bool:
        if not self.cookie_jar_shelf:
            logger.debug("No cookies found. Please log in first.")
            return False

        return all(
            self.cookie_jar_still_valid(cookie_jar, buffer_hours=buffer_hours)
            for cookie_jar in self.cookie_jar_shelf
        )

    @staticmethod
    def cookie_jar_still_valid(cookie_jar, buffer_hours=0) -> bool:
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=buffer_hours)
        cookies_have_expired = False
        for cookie in cookie_jar:
            if isinstance(cookie.expires, (float, int)):
                expires_time = datetime.datetime.utcfromtimestamp(cookie.expires)
            elif isinstance(cookie.expires, datetime.datetime):
                expires_time = cookie.expires
            else:
                continue

            if expires_time < now:
                logger.debug(f"Cookie {cookie.name} has expired.")
                cookies_have_expired = True

        cookie_jar_is_valid = not cookies_have_expired

        return cookie_jar_is_valid

    def get_remaining_validity(self):
        if not self.cookie_jar_shelf:
            logger.debug("No cookies found. Please log in first.")
            return False

        return min(
            [
                self.get_remaining_validity_cookie_jar(cookie_jar)
                for cookie_jar in self.cookie_jar_shelf
            ]
        )

    def get_remaining_validity_cookie_jar(self, cookie_jar):
        if cookie_jar is None:
            logger.info("No cookies found. Please log in first.")
            return 0

        minimum_time_delta = None
        for cookie in cookie_jar:
            if isinstance(cookie.expires, (float, int)):
                expires_time = datetime.datetime.utcfromtimestamp(cookie.expires)
            elif isinstance(cookie.expires, datetime.datetime):
                expires_time = cookie.expires
            else:
                continue

            time_delta = expires_time - datetime.datetime.utcnow()
            if minimum_time_delta is None or time_delta < minimum_time_delta:
                minimum_time_delta = time_delta

        if minimum_time_delta is None:
            # something large, like 10 years
            minimum_time_delta = datetime.timedelta(days=3650)

        return minimum_time_delta

    def reduce_number_of_cookie_jars_to(self, n):
        if n < len(self.cookie_jar_shelf):
            self.cookie_jar_shelf = self.cookie_jar_shelf[:n]

    def remove_expired_cookies(self):
        self.cookie_jar_shelf = [
            cookie_jar
            for cookie_jar in self.cookie_jar_shelf
            if self.cookie_jar_still_valid(cookie_jar)
        ]

        self.delete_cookie_files()
        self.save_to_file()

    def delete_cookie_files(self):
        if self.file_path is None:
            return None
        dir_path = os.path.dirname(self.file_path)
        base_name = os.path.basename(self.file_path)

        for item in os.listdir(dir_path):
            if item.endswith(".txt") and item.startswith(base_name):
                os.remove(os.path.join(dir_path, item))

        os.remove(self.file_path + ".yaml")

    def __call__(self):
        return self.cookies

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(cookie_jar_shelf={self.cookie_jar_shelf}, file_path={self.file_path})"
        )

    def __len__(self) -> int:
        return len(self.cookie_jar_shelf)

    def __iter__(self):
        return iter(self.cookie_jar_shelf)
