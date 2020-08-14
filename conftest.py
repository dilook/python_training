import configparser
import os

import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    config = read_config()

    global fixture
    browser = request.config.getoption("--browser")
    base_url_from_cli = request.config.getoption("--base_url")
    base_url = config['DEFAULT']['url'] if base_url_from_cli is None else base_url_from_cli
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--base_url", action="store", default=None)


def read_config():
    root_path = os.path.dirname(__file__)
    config = configparser.ConfigParser()
    setup_file = f"{root_path}{os.sep}setup.ini"
    config.read(setup_file)
    return config
