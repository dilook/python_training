# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app, db, data_contacts):
    old_contacts = db.get_contact_list()
    app.contact.add_new(data_contacts)
    assert len(old_contacts) + 1 == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    old_contacts.append(data_contacts)
    assert sorted(old_contacts, key=Contact.get_id_or_max) == sorted(new_contacts, key=Contact.get_id_or_max)
