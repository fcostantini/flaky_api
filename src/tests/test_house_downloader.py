from unittest import TestCase
from unittest.mock import Mock, patch

from ..house_downloader import HouseDownloader


def mocked_requests_get(url, **kwargs):
    class MockResponse:
        def __init__(self, json_response, status_code):
            self.json_response = json_response
            self.status_code = status_code

        def json(self):
            return self.json_response

    return MockResponse({"some_key": "some_value"}, 200)


class TestHouseDownloader(TestCase):
    def setUp(self):
        self.requests_library = Mock()
        self.house_page_processor = Mock()
        self.house_downloader = HouseDownloader(self.requests_library, self.house_page_processor)

    # Directory manipulation could also be done via a dependency and avoid this but wanted to
    # simplify the setup a bit
    @patch("os.mkdir", return_value=Mock())
    def test_download_houses_single_page(self, patched_mkdir):
        self.house_downloader.NUMBER_OF_PAGES = 1
        self.requests_library.get = Mock(side_effect=mocked_requests_get)
        self.house_page_processor.download_all.return_value = ["some_result1", "some_result2"]

        result = self.house_downloader.download_houses()

        self.assertEqual(result, ["some_result1", "some_result2"])
        self.house_page_processor.download_all.assert_called_once_with({"some_key": "some_value"})
