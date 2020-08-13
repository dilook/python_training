from random import randrange

from fixture.string_utils import merge_emails_like_on_homepage
from fixture.string_utils import merge_phones_like_on_homepage
from fixture.string_utils import prepare_link


def test_contact_on_edit_form(app):
    contacts_count = app.contact.count()
    index = randrange(contacts_count)
    print(index)
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.homepage == prepare_link(contact_from_edit_page.homepage)
