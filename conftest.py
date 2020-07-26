import configparser
import os

import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app():
    config = read_config()
    base_url = config['DEFAULT']['url']

    global fixture
    if fixture is None:
        fixture = Application(base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(base_url)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def read_config():
    root_path = os.path.dirname(__file__)
    config = configparser.ConfigParser()
    setup_file = f"{root_path}{os.sep}setup.ini"
    config.read(setup_file)
    return config
