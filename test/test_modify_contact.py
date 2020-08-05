from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(title="New_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(title="MODIFIED"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
