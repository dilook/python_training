# -*- coding: utf-8 -*-
import random

from model.contact import Contact
from model.group import Group
from utils.db_utils import clean_contact_name


def test_add_contact(app, db, data_contacts, check_ui, orm):
    old_contacts = orm.get_contact_list()
    app.contact.add_new(data_contacts)
    new_contacts = orm.get_contact_list()
    old_contacts.append(data_contacts)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(clean_contact_name, old_contacts), key=Contact.get_id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.get_id_or_max)


def test_add_contact_to_group(app, check_ui, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="SuperGroup"))
    if len(orm.get_contact_list()) == 0:
        app.contact.add_new(Contact(title="Belong SuperGroup"))
    contact = random.choice(orm.get_contact_list())
    group = random.choice(orm.get_group_list())
    app.contact.add_contact_to_group(contact.id, group)
    contacts = orm.get_contacts_in_group(group)
    assert contact in contacts

    if check_ui:
        app.contact.filter_by_group(group)
        filtered_list = [c for c in app.contact.get_contact_list() if c.id == contact.id]
        assert filtered_list[0] in contacts
