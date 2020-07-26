from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(title="New_contact"))
    app.contact.modify_first_contact(Contact(title="MODIFIED"))
