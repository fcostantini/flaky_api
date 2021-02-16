from concurrent.futures import ThreadPoolExecutor

from single_house_downloader import SingleHouseDownloader
from custom_types import House, JSONType


class HousePageProcessor:
    """Class that takes care of processing a single page of houses from the API.

    This spawns concurrent threads so that images can be downloaded in parallel.
    """
    def __init__(self, single_house_downloader: SingleHouseDownloader):
        self._single_house_downloader = single_house_downloader

    @classmethod
    def build(cls):
        return cls(SingleHouseDownloader.build())

    def download_all(self, page: JSONType):
        houses = []
        for house in page['houses']:
            house = House(id=house['id'], address=house['address'], url=house['photoURL'])
            houses.append(house)

        with ThreadPoolExecutor(max_workers=10) as executor:
            return executor.map(self._single_house_downloader.download_image, houses, timeout=60)

    # Alternative that does not use concurrency, just to see how long it would take
    def download_all_sequentially(self, page: JSONType):
        for house in page['houses']:
            house = House(id=house['id'], address=house['address'], url=house['photoURL'])
            yield self._single_house_downloader.download_image(house)
