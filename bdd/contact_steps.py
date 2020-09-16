import random

from pytest_bdd import given, when, then

from model.contact import Contact
from utils.db_utils import clean_contact_name


@given('a contact list', target_fixture="contact_list")
def contact_list(orm):
    return orm.get_contact_list()


@given('a contact with <first_name>, <last_name>', target_fixture="new_contact")
def new_contact(first_name, last_name):
    return Contact(first_name=first_name, last_name=last_name)


@when('I add the contact to the list')
def add_contact(app, new_contact):
    app.contact.add_new(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_list(orm, app, check_ui, new_contact, contact_list):
    old_contacts = contact_list
    new_contacts = orm.get_contact_list()
    old_contacts.append(new_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(clean_contact_name, old_contacts), key=Contact.get_id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.get_id_or_max)


@given('a non-empty contact list', target_fixture="non_empty_contact_list")
def non_empty_contact_list(app, db):
    if len(db.get_group_list()) == 0:
        app.contact.add_new(Contact(title="New_contact"))
    return db.get_contact_list()


@given("a random contact from the list", target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then("the new contact list is equal to the old list without the deleted contact")
def verify_contact_deleted(db, random_contact, non_empty_contact_list, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        db_list = map(clean_contact_name, old_contacts)
        assert sorted(db_list, key=Contact.get_id_or_max) == sorted(app.contact.get_contact_list(),
                                                                    key=Contact.get_id_or_max)


@when("I modify the contact from the list")
def modify_contact(random_contact, app):
    random_contact.firstname = "MODIFIED"
    random_contact.lastname = "MIMI"
    app.contact.modify_contact(random_contact)


@then("the new contact list is equal to the old list with the modified contact")
def verify_modified_contact(app, db, check_ui, non_empty_contact_list):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(clean_contact_name, old_contacts), key=Contact.get_id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.get_id_or_max)
