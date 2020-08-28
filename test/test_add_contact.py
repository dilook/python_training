# -*- coding: utf-8 -*-

from model.contact import Contact
from utils.db_utils import clean_contact_name


def test_add_contact(app, db, data_contacts, check_ui):
    old_contacts = db.get_contact_list()
    app.contact.add_new(data_contacts)
    new_contacts = db.get_contact_list()
    old_contacts.append(data_contacts)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(clean_contact_name, old_contacts), key=Contact.get_id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.get_id_or_max)
