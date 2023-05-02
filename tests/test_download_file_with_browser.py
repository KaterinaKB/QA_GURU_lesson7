import os
import time
from selene import browser
from conftest import TMP_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp


def test_download_file_with_browser(set_browser_options):
    browser.open("https://github.com/pytest-dev/pytest")

    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)

    size = os.path.getsize(os.path.join(TMP_PATH, "pytest-main.zip"))
    assert size == 1565002
