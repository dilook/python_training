# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    new_contact = Contact(first_name="Dia", middle_name="Korret", last_name="Medercy", nick="dia",
                          mobile_phone="+45135464151", work_phone="45-49-45", email="test@test.com", day="1",
                          month="April", year="1978", company="Google", address="25 Korovina str",
                          homepage="humster.com", group="[none]", title="Dia")
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(new_contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(Contact())
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
