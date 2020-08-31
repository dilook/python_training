import random

from model.contact import Contact
from model.group import Group
from utils.db_utils import clean_contact_name


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.add_new(Contact(title="New_contact"))
    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(selected_contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(selected_contact)
    assert old_contacts == new_contacts
    db_list = map(clean_contact_name, old_contacts)
    if check_ui:
        assert sorted(db_list, key=Contact.get_id_or_max) == sorted(app.contact.get_contact_list(),
                                                                    key=Contact.get_id_or_max)


def test_remove_contact_from_group(app, check_ui, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="SuperGroup"))
    if len(orm.get_contact_list()) == 0:
        app.contact.add_new(Contact(title="Belong SuperGroup"))
    (contact, group) = get_contact_in_group(orm)
    if contact is None and group is None:
        contact = random.choice(orm.get_contact_list())
        group = random.choice(orm.get_group_list())
        app.contact.add_contact_to_group(contact.id, group)

    app.contact.remove_contact_from_group(contact.id, group)
    assert contact in orm.get_contacts_not_in_group(group)
    if check_ui:
        app.contact.filter_by_group(group)
        assert contact not in app.contact.get_contact_list()


def get_contact_in_group(orm):
    for gr in orm.get_group_list():
        contacts = orm.get_contacts_in_group(gr)
        if len(contacts) > 0:
            contact = contacts[0]
            group = gr
            return contact, group
    return None, None
