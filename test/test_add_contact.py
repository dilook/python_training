# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    new_contact = Contact(first_name="Dia", middle_name="Korret", last_name="Medercy", nick="dia",
                          mobile_phone="+45135464151", work_phone="45-49-45", email="test@test.com", day="1",
                          month="April", year="1978", company="Google", address="25 Korovina str",
                          homepage="humster.com", group="[none]", title="Dia")
    app.contact.add_new(new_contact)
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact())
    app.session.logout()
