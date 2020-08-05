from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(title="New_contact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="MODIFIED", last_name="MIMI")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.get_id_or_max) == sorted(new_contacts, key=Contact.get_id_or_max)
