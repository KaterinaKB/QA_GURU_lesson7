import os
import pytest
from selenium import webdriver
from selene import browser

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
TMP_PATH = os.path.join(PROJECT_ROOT_PATH, "tmp")
RESOURSES_PATH = os.path.join(PROJECT_ROOT_PATH, "resources")


@pytest.fixture()
def create_tmp_directory():
    if not os.path.exists(TMP_PATH):
        os.mkdir(TMP_PATH)


@pytest.fixture()
def set_browser_options(create_tmp_directory):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_PATH,
        "download.prompt_for_download": False,
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options
