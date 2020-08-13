# -*- coding: utf-8 -*-
import pytest

from fixture.string_utils import random_phone
from fixture.string_utils import random_string
from fixture.string_utils import random_site
from fixture.string_utils import random_email
from model.contact import Contact

testdata = [Contact(first_name="", last_name="")] + [
    Contact(first_name=random_string("name", 10), middle_name=random_string("third", 12),
            last_name=random_string("surname", 15), nick=random_string("nick", 10),
            mobile_phone=random_phone(11), work_phone=random_phone(11), secondary_phone=random_phone(11),
            home_phone=random_phone(11), email=random_email(15), email2=random_email(15), email3=random_email(15),
            day="1", month="April", year="1978", company=random_string("surname", 10), address=random_string("addr", 56),
            homepage=random_site(16), title=random_string("surname", 10))
    for i in range(5)
]


@pytest.mark.parametrize("new_contact", testdata, ids=[repr(i) for i in testdata])
def test_add_contact(app, new_contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.get_id_or_max) == sorted(new_contacts, key=Contact.get_id_or_max)
