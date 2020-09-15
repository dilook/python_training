from pytest_bdd import given

from model.contact import Contact


@given('a contact list')
def contact_list(orm):
    return orm.get_contact_list()


@given('a contact with <first name>, <last name>')
def new_contact(first_name, last_name):
    return Contact(first_name=first_name, last_name=last_name)
