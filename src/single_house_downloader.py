from pathlib import Path
from typing import Callable
from urllib import request

from custom_types import House


class SingleHouseDownloader:
    """Class that takes care of downloading a single image and save it locally."""
    OUTPUT_DIRECTORY = "output/"

    # Instead of using a function as a dependency it could be the whole module or a new class that
    # implements the same behavior. Decided to go this way just cause it's simpler
    def __init__(self, retrieve_file_from_url: Callable[[str, str], None]):
        self._retrieve_file_from_url = retrieve_file_from_url

    @classmethod
    def build(cls):
        return cls(request.urlretrieve)

    def download_image(self, house: House) -> str:
        image_url = house.url
        full_file_path = Path(image_url)
        file_extension = full_file_path.suffix
        file_name = f"id-{house.id}-{house.address}{file_extension}"
        output_path = f"{self.OUTPUT_DIRECTORY}{file_name}"

        self._retrieve_file_from_url(image_url, output_path)

        result_message = f"Finished downloading {output_path}"

        return result_message
