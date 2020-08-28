import random

from model.contact import Contact
from utils.db_utils import clean_contact_name


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(title="New_contact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.firstname = "MODIFIED"
    contact.lastname = "MIMI"
    app.contact.modify_contact(contact)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(clean_contact_name, old_contacts), key=Contact.get_id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.get_id_or_max)
