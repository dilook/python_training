import configparser
import os

import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    config = read_config()
    base_url = config['DEFAULT']['url']
    fixture = Application(base_url)
    request.addfinalizer(fixture.destroy)
    return fixture


def read_config():
    root_path = os.path.dirname(__file__)
    config = configparser.ConfigParser()
    setup_file = f"{root_path}{os.sep}setup.ini"
    config.read(setup_file)
    return config
