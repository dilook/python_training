import random

from model.contact import Contact
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
