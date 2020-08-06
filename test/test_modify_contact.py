from random import randrange

from model.contact import Contact


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(title="New_contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="MODIFIED", last_name="MIMI")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.get_id_or_max) == sorted(new_contacts, key=Contact.get_id_or_max)
