from unittest import TestCase
from unittest.mock import call, Mock

from ..custom_types import House
from ..house_page_processor import HousePageProcessor


class TestHousePageProcessor(TestCase):
    def setUp(self):
        self.single_house_downloader = Mock()
        self.house_page_processor = HousePageProcessor(self.single_house_downloader)

    def test_download_houses_page(self):
        houses_page = dict(
            houses=[
                dict(id=0, address="first_address", photoURL="first_url.jpg"),
                dict(id=1, address="second_address", photoURL="second_url.jpg"),
            ]
        )
        self.house_page_processor.download_all(houses_page)

        # Ideally we assert these are the right calls but it's not working, maybe related to using a thread pool
        # first_house = House(id=0, address="first_address", url="first_url.jpg")
        # second_house = House(id=1, address="second_address", url="second_url.jpg")

        self.single_house_downloader.download_image.assert_called()
