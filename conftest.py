import configparser
import os

import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = get_run_parameter("browser", request)
    user = get_run_parameter("user", request)
    password = get_run_parameter("password", request)
    base_url = get_run_parameter("base_url", request)
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username=user, password=password)
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
    parser.addoption("--base_url", action="store")
    parser.addoption("--user", action="store")
    parser.addoption("--password", action="store")


def read_config():
    root_path = os.path.dirname(__file__)
    config = configparser.ConfigParser()
    setup_file = f"{root_path}{os.sep}setup.ini"
    config.read(setup_file)
    return config


def get_run_parameter(name, request):
    config = read_config()
    param_from_cli = request.config.getoption(f"--{name}")
    return config['DEFAULT'][name] if param_from_cli is None else param_from_cli
