import os.path
import requests
from conftest import TMP_PATH


def test_downloaded_file_size(create_tmp_directory):
    # TODO сохранять и читать из tmp, использовать универсальный путь

    url = "https://selenium.dev/images/selenium_logo_square_green.png"

    r = requests.get(url)
    with open(os.path.join(TMP_PATH, "selenium_logo.png"), "wb") as file:
        file.write(r.content)

    size = os.path.getsize(os.path.join(TMP_PATH, "selenium_logo.png"))

    assert size == 30803
