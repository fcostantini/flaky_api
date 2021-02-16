from unittest import TestCase
from unittest.mock import Mock

from ..custom_types import House
from ..single_house_downloader import SingleHouseDownloader


class TestSingleHouseDownloader(TestCase):
    def setUp(self):
        self.retrieve_file_from_url = Mock()
        self.single_house_downloader = SingleHouseDownloader(self.retrieve_file_from_url)

    def test_download_image(self):
        house = House(id=13, address="some_address", url="some_url.jpg")
        self.single_house_downloader.download_image(house)
        self.retrieve_file_from_url.assert_called_once_with("some_url.jpg", "output/id-13-some_address.jpg")
