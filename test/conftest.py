from email.policy import default

import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.remote.webdriver import WebDriver


def new_driver(hub_host: str, options: BaseOptions) -> WebDriver:
    return webdriver.Remote(
        command_executor=hub_host,
        options=options
    )


def pytest_addoption(parser):
    parser.addoption(
        "--hub-host", type=str, default="http://localhost/wd/hub"
    )


def pytest_generate_tests(metafunc):
    if "_driver_opts" in metafunc.fixturenames:
        metafunc.parametrize("_driver_opts", [ChromeOptions(), FirefoxOptions(), EdgeOptions()])
    if "_hub_host" in metafunc.fixturenames:
        metafunc.parametrize("_hub_host", [metafunc.config.getoption("hub_host")])

@pytest.fixture()
def driver(_hub_host, _driver_opts) -> WebDriver:
    _driver = new_driver(_hub_host, _driver_opts)
    try:
        yield _driver
    finally:
        _driver.quit()
