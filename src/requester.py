from abc import abstractmethod, ABC
from typing import Optional

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Requester(ABC):
    """Interface that allows using the requests library with different implementations.

    Only implements GET because that's the only method we need for this script, but could easily be
    extended to support every required method.
    """
    @abstractmethod
    def get(self, url: str, **kwargs) -> requests.Response:
        pass


RetryError = requests.exceptions.RetryError


class RequestsLibrary(Requester):
    """Implements the Requester interface using the requests library."""

    def __init__(self, session: Optional[requests.Session] = None):
        self._session = session if session is not None else requests.session()
        self._set_retry_strategy()

    def get(self, url: str, **kwargs) -> requests.Response:
        """Issue a GET request.

        Also uses a session to bind all HTTP requests to the same connection. See https://requests.readthedocs.io/en/master/user/advanced/
        """
        return self._session.get(url, **kwargs)

    def _set_retry_strategy(self):
        """Set a retry strategy so failures on the request get handled automatically."""
        retry_strategy = Retry(
            total=5,
            # The values below are specific to this project but they could be extended to consider more cases easily
            status_forcelist=[429, 500],
            method_whitelist=["GET"],
            backoff_factor=1,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self._session.mount("http://", adapter)
