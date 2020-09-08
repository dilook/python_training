from random import randrange

from fixture.string_utils import merge_emails_like_on_homepage
from fixture.string_utils import merge_phones_like_on_homepage
from fixture.string_utils import prepare_link


def test_contact_on_edit_form(app, orm):
    contacts_from_home_page = app.contact.get_contact_list()
    for contact in contacts_from_home_page:
        contact_from_db = orm.get_contact_by_id(contact.id)
        assert contact.all_phones == merge_phones_like_on_homepage(contact_from_db)
        assert contact.all_emails == merge_emails_like_on_homepage(contact_from_db)
        assert contact.firstname == contact_from_db.firstname
        assert contact.lastname == contact_from_db.lastname
        assert contact.address == contact_from_db.address
        assert contact.homepage == prepare_link(contact_from_db.homepage)
