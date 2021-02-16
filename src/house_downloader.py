import os

from house_page_processor import HousePageProcessor
from requester import Requester, RequestsLibrary, RetryError
from time_util import timeit


class HouseDownloader:
    """Class that takes care of downloading the images for the given range of houses from the API.

    It does so by iterating through the first 10 pages of the API endpoint and processing each page
    to download the images.
    """
    NUMBER_OF_PAGES = 10
    API_URL = "http://app-homevision-staging.herokuapp.com/api_project/houses"

    def __init__(self, requests_library: Requester, house_page_processor: HousePageProcessor):
        self._requests_library = requests_library
        self._house_page_processor = house_page_processor

    @classmethod
    def build(cls):
        return cls(RequestsLibrary(), HousePageProcessor.build())

    @timeit
    def download_houses(self):
        self._ensure_dir()

        results = []
        for i in range(1, self.NUMBER_OF_PAGES+1):
            # I think this could also be parallelized as a further improvement, no real reason we
            # have to access the pages sequentially
            url = f"{self.API_URL}?page={i}"
            try:
                response = self._requests_library.get(url)
            except RetryError:  # We allow for 5 retries which should always be enough but if not we log it
                print(f"Page {i} could not be loaded after the maximum amount of retries.")
                continue

            page_results = self._house_page_processor.download_all(response.json())
            for page_result in page_results:
                results.append(page_result)

        return results

    def _ensure_dir(self):
        if not os.path.isdir("output"):
            os.mkdir("output")
