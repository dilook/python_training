# -*- coding: utf-8 -*-
import pytest

from data.contacts import testdata
from model.contact import Contact


@pytest.mark.parametrize("new_contact", testdata, ids=[repr(i) for i in testdata])
def test_add_contact(app, new_contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.get_id_or_max) == sorted(new_contacts, key=Contact.get_id_or_max)
