# -*- coding: utf-8 -*-
import pytest

from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    new_contact = Contact(first_name="Dia", middle_name="Korret", last_name="Medercy", nick="dia",
                          day="1", month="April", year="1978",
                          work_phone="45-49-45", mobile_phone="+45135464151", email="test@test.com",
                          company="Google", address="25 Korovina str", homepage="humster.com",
                          group="[none]", title="Dia"
                          )
    app.add_new_contact(new_contact)
    app.logout()
