import importlib
import json
import os

import jsonpickle
import pytest

from fixture.application import Application
from fixture.db import DbFixture
from fixture.orm import ORMFixture

db_fixture = None
orm_fixture = None
fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(file) as config_file:
            target = json.load(config_file)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["base_url"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        try:
            fixture.session.ensure_logout()
        finally:
            fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    global db_fixture
    if db_fixture is None:
        db_fixture = DbFixture(host=db_config["host"], port=db_config["port"], db_name=db_config["db_name"],
                               user=db_config["user"], password=db_config["password"])

    def fin():
        db_fixture.destroy()

    request.addfinalizer(fin)
    return db_fixture


@pytest.fixture(scope="session")
def orm(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    global orm_fixture
    if orm_fixture is None:
        orm_fixture = ORMFixture(host=db_config["host"], port=db_config["port"], name=db_config["db_name"],
                                 user=db_config["user"], password=db_config["password"])

    # def fin():
    #     orm_fixture.destroy()
    #
    # request.addfinalizer(fin)
    return orm_fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def load_from_module(module):
    return importlib.import_module(f"data.{module}").testdata


def load_from_json(file_name):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", f"{file_name}.json")
    with open(file) as f:
        return jsonpickle.decode(f.read())


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
