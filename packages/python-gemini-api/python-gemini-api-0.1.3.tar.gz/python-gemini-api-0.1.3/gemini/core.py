# Copyright 2024 Minwoo(Daniel) Park, MIT License
import os
import re
import json
import time
import requests
import aiohttp
import asyncio
from typing import Optional, Any, List

try:
    from deep_translator import GoogleTranslator
    from google.cloud import translate_v2 as translate
except ImportError:
    pass

from .constants import (
    REQUIRED_COOKIE_LIST,
    HEADERS,
    HOST,
    SHARE_HEADERS,
    SHARE_ENDPOINT,
    POST_ENDPOINT,
    SUPPORTED_BROWSERS,
    Tool,
)
from .models.base import (
    GeminiOutput,
)
from .models.exceptions import (
    TimeoutError,
)


class Gemini:
    """
    Represents a Gemini instance for interacting with various services. It supports features like automatic cookie handling, proxy configuration, Google Cloud Translation integration, and optional code execution within IPython environments.

    Attributes:
        session (requests.Session): A session object for making HTTP requests.
        cookies (dict): A dictionary containing cookies with their respective values, important for maintaining session state.
        timeout (int): Request timeout in seconds, defaults to 30.
        proxies (Optional[dict]): Proxy configuration for requests, useful for routing requests through specific network interfaces.
        language (Optional[str]): Code for the natural language for translation services (e.g., "en", "ko", "ja").
        auto_cookies (bool): Indicates whether to automatically retrieve and manage cookies, defaults to False.
        google_translator_api_key (Optional[str]): The Google Cloud Translation API key for translation services.
        run_code (bool): Indicates whether to execute code included in the response, applicable only in IPython environments.
        verify (bool): Whether to verify SSL certificates for HTTPS requests.
    """

    __slots__ = [
        "session",
        "token",
        "cookies",
        "timeout",
        "proxies",
        "language",
        "auto_cookies",
        "google_translator_api_key",
        "run_code",
        "share_session",
        "verify",
    ]

    def __init__(
        self,
        auto_cookies: bool = False,
        token: str = None,
        session: Optional[requests.Session] = None,
        share_session: Optional[requests.Session] = None,
        cookies: Optional[dict] = None,
        timeout: int = 30,
        proxies: Optional[dict] = None,
        language: Optional[str] = None,
        google_translator_api_key: Optional[str] = None,
        run_code: bool = False,
        verify: bool = True,
    ):
        """
        Initializes a new instance of the Gemini class, setting up the necessary configurations for interacting with the services.

        Parameters:
            auto_cookies (bool): Whether to automatically manage cookies.
            token (Optional[str]): Authentication token for the session.
            session (Optional[requests.Session]): A custom session object. If not provided, a new session will be created.
            share_session (Optional[requests.Session]): A session object to be shared among instances, if applicable.
            cookies (Optional[dict]): Initial cookie values. If auto_cookies is True, cookies are managed automatically.
            timeout (int): Request timeout in seconds, defaults to 30.
            proxies (Optional[dict]): Proxy configurations for the requests.
            language (Optional[str]): Default language for translation services.
            google_translator_api_key (Optional[str]): Google Cloud Translation API key.
            run_code (bool): Flag indicating whether to execute code in IPython environments.
            verify (bool): Whether to verify SSL certificates for HTTPS requests.
        """
        self.auto_cookies = auto_cookies
        self.cookies = cookies or {}
        self._set_cookies(auto_cookies)
        self.proxies = proxies or {}
        self.timeout = timeout
        self.session = self._set_session(session)
        self.share_session = self._set_share_session(share_session)
        self.token = token
        self.token = self.get_nonce_value()
        self.language = language or os.getenv("GEMINI_LANGUAGE")
        self.google_translator_api_key = google_translator_api_key
        self.run_code = run_code
        self.verify = verify

    def check_session_cookies(self) -> None:
        """
        Prints the session's cookies. Indicates if the session is uninitialized.
        """
        if self.session:
            cookies = self.session.cookies.get_dict()
            cookies_str = "\n".join(f"{key}: {value}" for key, value in cookies.items())
            print(f"Session Cookies:\n{cookies_str}")
        else:
            print("Session not initialized.")

    def check_session_headers(self) -> None:
        """
        Prints the session's headers. Indicates if the session is uninitialized.
        """
        if self.session:
            headers = self.session.headers
            headers_str = "\n".join(f"{key}: {value}" for key, value in headers.items())
            print(f"Session Headers:\n{headers_str}")
        else:
            print("Session not initialized.")

    def _set_cookies_from_browser(self) -> None:
        """
        Extracts Gemini cookies from web browsers' cookies on the system for a specific domain (".google.com").

        Iterates over supported browsers to add found cookies to the instance's cookie store. Supports multiple browsers and OS.

        Updates `cookies` attribute with found cookies.

        Raises:
            ValueError: If essential cookies are missing after checking all supported browsers.
        """
        for browser_fn in SUPPORTED_BROWSERS:
            try:
                print(f"Retrieving cookies from {browser_fn} via browser_cookie3.")
                cj = browser_fn(domain_name=".google.com")
                self.cookies.update({cookie.name: cookie.value for cookie in cj})
            except Exception:
                continue  # Try the next browser if an exception occurs

        if not self.cookies:
            raise ValueError(
                "Failed to get cookies. Ensure 'auto_cookies' is True or manually set 'cookies'."
            )

        missing_cookies = set(REQUIRED_COOKIE_LIST) - self.cookies.keys()
        if missing_cookies:
            print(f"Missing recommended cookies: {', '.join(missing_cookies)}.")

    def _set_cookies(self, auto_cookies: bool) -> None:
        """
        Updates the instance's cookies attribute with Gemini API tokens, either from environment variables or by extracting them from the browser, based on the auto_cookies flag.

        Args:
            auto_cookies (bool): Indicates whether to attempt automatic extraction of tokens from the browser's cookies.

        Raises:
            Exception: If no cookies are provided through environment variables or cannot be extracted from the browser when auto_cookies is True.
        """
        if not self.cookies:
            self.cookies.update(
                {
                    cookie: os.getenv(cookie)
                    for cookie in REQUIRED_COOKIE_LIST
                    if os.getenv(cookie)
                }
            )

        if auto_cookies and not self.cookies:
            try:
                self._set_cookies_from_browser()  # Assuming this updates self.cookies directly
            except Exception as e:
                raise Exception("Failed to extract cookies from browser.") from e
        if not auto_cookies and not self.cookies:
            print(
                "Cookie loading issue, try setting auto_cookies to True. Restart browser, log out, log in for Gemini Web UI to work. Keep a single browser open."
            )
        if not self.cookies:
            raise Exception(
                "Gemini cookies must be provided through environment variables or extracted from the browser with auto_cookies enabled."
            )

    def _set_session(
        self, session: Optional[requests.Session] = None
    ) -> requests.Session:
        """
        Initializes or uses a provided requests.Session object. If a session is not provided, a new one is created.
        The new or provided session is configured with predefined session headers, proxies, and cookies from the instance.

        Args:
            session (Optional[requests.Session]): An optional requests.Session object. If provided, it will be used as is; otherwise, a new session is created.

        Returns:
            requests.Session: The session object, either the one provided or a newly created and configured session.

        Raises:
            ValueError: If 'session' is None and the 'cookies' dictionary is empty, indicating that there's insufficient information to properly set up a new session.
        """
        if session is not None:
            return session

        if not self.cookies:
            raise ValueError("Failed to set session. 'cookies' dictionary is empty.")

        session = requests.Session()
        session.headers.update(
            HEADERS
        )  # Use `update` to ensure we're adding to any existing headers
        session.proxies.update(self.proxies)
        session.cookies.update(self.cookies)

        return session

    def _set_share_session(
        self, session: Optional[requests.Session] = None
    ) -> requests.Session:
        """
        Initializes or uses a provided requests.Session object. If a session is not provided, a new one is created.
        The new or provided session is configured with predefined session headers, proxies, and cookies from the instance.

        Args:
            session (Optional[requests.Session]): An optional requests.Session object. If provided, it will be used as is; otherwise, a new session is created.

        Returns:
            requests.Session: The session object, either the one provided or a newly created and configured session.

        Raises:
            ValueError: If 'session' is None and the 'cookies' dictionary is empty, indicating that there's insufficient information to properly set up a new session.
        """
        if session is not None:
            return session

        if not self.cookies:
            raise ValueError("Failed to set session. 'cookies' dictionary is empty.")

        session = requests.Session()
        session.headers.update(
            SHARE_HEADERS
        )  # Use `update` to ensure we're adding to any existing headers
        session.proxies.update(self.proxies)
        session.cookies.update(self.cookies)

        return session

    def get_nonce_value(self) -> str:
        """
        Get the Nonce Token value from the Gemini API response.

        Returns:
            str: Nonce value.
        Raises:
            Exception: If the __Secure-1PSID value is invalid or token value is not found in the response.
        """
        response = self.session.get(HOST, timeout=self.timeout, proxies=self.proxies)
        if response.status_code != 200:
            raise Exception(
                f"Response status code is not 200. Response Status is {response.status_code}"
            )
        nonce = re.findall(r'nonce="([^"]+)"', response.text)
        if nonce == None:
            raise Exception(
                "Nonce not found. Check cookies or set 'auto_cookies' to True. \nCookie needs vary by location/account. Often due to cookie updates. \nIf set correctly need cookies, restart browser, re-login, or refresh cookie manually."
            )
        return nonce

    def _prepare_data(self, prompt, gemini_session=None):
        data = {
            "at": self.token,
            "f.req": json.dumps(
                [
                    None,
                    json.dumps(
                        [[prompt], None, gemini_session and gemini_session.metadata]
                    ),
                ]
            ),
            "rpcids": "ESY5D",
        }
        return data

    def _execute_prompt(
        self,
        prompt: str,
        gemini_session: Optional["GeminiSession"] = None,
    ) -> dict:
        """
        Generates content by querying the Gemini API, supporting text and optional image input alongside a specified tool for content generation.

        Args:
            prompt (str): The input text for the content generation query.
            session (Optional[GeminiSession]): A session object for the Gemini API, if None, a new session is created or a default session is used.
            image (Optional[bytes]): Input image bytes for the query; supported image types include JPEG, PNG, and WEBP. This parameter is optional and used for queries that benefit from image context.
            tool (Optional[Tool]): The tool to use for content generation, specifying the context or platform for which the content is relevant. Options include Gmail, Google Docs, Google Drive, Google Flights, Google Hotels, Google Maps, and YouTube. This parameter is optional.

        Returns:
            dict: A dictionary containing the response from the Gemini API, which may include content, conversation ID, response ID, factuality queries, text query, choices, links, images, programming language, code, and status code.
        """
        data = self._prepare_data(prompt, gemini_session)
        data["rpcids"] = "ESY5D"

        # Post request that cannot receive any response due to Google changing the logic for the Gemini API Post to the Web UI.
        try:
            execute_response = self.session.post(
                POST_ENDPOINT,
                data=data,
                timeout=self.timeout,
                proxies=self.proxies,
                verify=self.verify,
            )
            execute_response.raise_for_status()  # Raises a HTTPError for bad responses
        except requests.exceptions.Timeout as e:
            raise TimeoutError(
                f"Request timed out: {e}. Increase the timeout parameter if this error persists."
            )
        except requests.exceptions.HTTPError as e:
            raise Exception(
                f"HTTP error occurred: {e}. Check the POST_ENDPOINT and network connectivity."
            )
        except requests.exceptions.RequestException as e:
            raise Exception(
                f"Error during request: {e}. Check your network connectivity and proxy settings."
            )

        return execute_response

    def generate_content(
        self,
        prompt: str,
        gemini_session: Optional["GeminiSession"] = None,
        wait_time: int = 40,
        retry_interval: int = 5,
    ) -> dict:
        """
        Generates content by querying the Gemini API, supporting text and optional session input. Attempts are made at fixed intervals within a total wait time of 40 seconds.

        Args:
            prompt (str): The input text for the content generation query.
            gemini_session (Optional[GeminiSession]): A session object for the Gemini API, if None, a new session is created or a default session is used.
            wait_time (int): Maximum time to wait for a successful response before timing out, default is 40 seconds.
            retry_interval (int): Time in seconds between each retry attempt, default is 5 seconds.

        Returns:
            dict: A dictionary containing the response from the Gemini API, which may include content, conversation ID, response ID, factuality queries, text query, choices, links, images, programming language, code, and status code.
        """
        attempts = wait_time // retry_interval
        for attempt in range(attempts):
            try:
                execute_response = self._execute_prompt(prompt, gemini_session)
                if execute_response.get("status_code") == 200:
                    print("Received status code 200. Processing response.")
                    return execute_response
                else:
                    print(
                        f"Attempt {attempt + 1}: Current execution status: {execute_response.get('status_code')}"
                    )
            except Exception as e:
                print(f"Attempt {attempt + 1}: Failed to process request: {e}")

            if attempt < attempts - 1:
                time.sleep(
                    retry_interval
                )  # Wait before retrying unless it's the last attempt

        print(
            f"Reached maximum attempts without success. Last status code: {execute_response.get('status_code', 'N/A')}"
        )
        return execute_response

    async def request_share(
        self,
    ) -> dict:
        """
        Asynchronously generates content by querying the Gemini API, supporting text and optional image input alongside a specified tool for content generation.

        Args:
            session (Optional[GeminiSession]): A session object for the Gemini API, if None, a new session is created or a default session is used.

        Returns:
            dict: A dictionary containing the response from the Gemini API.
        """
        url = SHARE_ENDPOINT

        async with aiohttp.ClientSession() as client:
            try:
                async with client.post(url, timeout=self.timeout) as response:
                    return await response.json()
            except asyncio.TimeoutError:
                raise TimeoutError(
                    "Request timed out. If errors persist, increase the timeout parameter in the Gemini class to a higher number of seconds."
                )


class GeminiSession:
    """
    Represents a session to manage and retrieve conversation history in the context of Gemini services. This class facilitates interaction with the Gemini API, allowing for the retrieval of conversation history based on specified metadata identifiers.

    Attributes:
        gemini (Gemini): An instance of the Gemini client interface used for interactions with https://gemini.google.com/. This attribute is essential for making API calls and retrieving data.
        __metadata (list[str], optional): A list of strings representing chat metadata, potentially including chat ID (`cid`), reply ID (`rid`), and reply candidate ID (`rcid`). This list can vary in length, accommodating fewer than three elements to match provided identifiers.
        gemini_output: Stores the output from the Gemini API calls. This attribute is managed internally and populated based on interactions facilitated by the session.

    Parameters:
        gemini (Gemini): The Gemini client interface, providing the necessary functionality to interact with the Gemini API.
        metadata (list[str], optional): A list containing identifiers for chat metadata, such as `[cid, rid, rcid]`. The list can be shorter, with one or two elements like `[cid]` or `[cid, rid]`, depending on the available information.
        cid (str, optional): A specific chat ID. If provided along with `metadata`, it will replace the first element in the metadata list, signifying the chat ID.
        rid (str, optional): A specific reply ID. If provided along with `metadata`, it will replace the second element in the metadata list, indicating the reply ID.
        rcid (str, optional): A specific reply candidate ID. If provided along with `metadata`, it will replace the third element in the metadata list, denoting the reply candidate ID.

    The class requires a Gemini instance to function correctly. It uses the provided metadata, along with optional specific identifiers (`cid`, `rid`, `rcid`), to manage and retrieve conversation history. Only when all three identifiers are provided will the complete conversation history be retrieved.
    """

    __slots__ = ["__metadata", "gemini", "gemini_output"]

    def __init__(
        self,
        gemini: Gemini,
        metadata: Optional[List[str]] = None,
        cid: Optional[str] = None,  # chat id
        rid: Optional[str] = None,  # reply id
        rcid: Optional[str] = None,  # reply candidate id
    ):
        self.__metadata: list[Optional[str]] = [None, None, None]
        self.gemini: Gemini = gemini
        self.gemini_output: Optional[GeminiOutput] = None

        if metadata:
            self.metadata = metadata
        if cid:
            self.cid = cid
        if rid:
            self.rid = rid
        if rcid:
            self.rcid = rcid

    def __str__(self):
        return f"GeminiSession(cid='{self.cid}', rid='{self.rid}', rcid='{self.rcid}')"

    __repr__ = __str__

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)
        if name == "gemini_output" and isinstance(value, GeminiOutput):
            self.metadata = value.metadata
            self.rcid = value.rcid

    def send_message(self, prompt: str) -> GeminiOutput:
        """
        Generates content by submitting a prompt to the Gemini API, acting as a shortcut method for `Gemini.generate_content(prompt, self)`.

        This method simplifies the process of content generation by directly accepting a user-provided prompt and leveraging the Gemini API to generate relevant content. The output encompasses a variety of content forms, including text responses, images, and a list of all answer candidates.

        Parameters:
            prompt (str): The input text provided by the user, serving as the basis for content generation.

        Returns:
            GeminiOutput: An object encapsulating the output data from gemini.google.com. The `GeminiOutput` object offers several attributes for accessing different parts of the response:
                - `text` for retrieving the default text reply.
                - `images` for obtaining a list of images included in the default reply.
                - `candidates` for accessing a comprehensive list of all answer candidates within the gemini_output.

        The method ensures a streamlined interface for interacting with the Gemini API, facilitating the retrieval of diverse content types based on the input prompt.
        """
        return self.gemini.generate_content(prompt, self)

    def choose_candidate(self, index: int) -> GeminiOutput:
        """
        Selects a specific candidate from the most recent `GeminiOutput` to direct the flow of an ongoing conversation.

        This method allows the user to influence the direction of the conversation by choosing one of the answer candidates provided by the last Gemini API call. By specifying the index of the desired candidate, the conversation can be steered towards a particular topic or response style.

        Parameters:
            index (int): The zero-based index of the candidate to be selected. This index corresponds to the position of the candidate within the list of answer candidates provided in the last `GeminiOutput`.

        The chosen candidate will affect subsequent interactions with the Gemini API, guiding the content and responses generated based on the selected conversational path.
        """
        if not self.gemini_output:
            raise ValueError(
                "No previous gemini_output data found in this chat session."
            )

        if index >= len(self.gemini_output.candidates):
            raise ValueError(
                f"Index {index} exceeds the number of candidates in last model gemini_output."
            )

        self.gemini_output.chosen = index
        self.rcid = self.gemini_output.rcid
        return self.gemini_output

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value: List[str]):
        if len(value) > 3:
            raise ValueError("metadata cannot exceed 3 elements")
        self.__metadata[: len(value)] = value

    @property
    def cid(self):
        return self.__metadata[0]

    @cid.setter
    def cid(self, value: str):
        self.__metadata[0] = value

    @property
    def rid(self):
        return self.__metadata[1]

    @rid.setter
    def rid(self, value: str):
        self.__metadata[1] = value

    @property
    def rcid(self):
        return self.__metadata[2]

    @rcid.setter
    def rcid(self, value: str):
        self.__metadata[2] = value
