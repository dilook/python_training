from fixture.string_utils import merge_emails_like_on_homepage
from fixture.string_utils import merge_phones_like_on_homepage
from fixture.string_utils import prepare_link
from utils.db_utils import clean_contact_name


def test_contact_on_edit_form(app, orm):
    contacts_from_home_page = app.contact.get_contact_list()
    for contact in contacts_from_home_page:
        contact_from_db = orm.get_contact_by_id(contact.id)
        stripped_contact = clean_contact_name(contact_from_db)
        assert contact.all_phones == merge_phones_like_on_homepage(stripped_contact)
        assert contact.all_emails == merge_emails_like_on_homepage(stripped_contact)
        assert contact.firstname == stripped_contact.firstname
        assert contact.lastname == stripped_contact.lastname
        assert contact.address == stripped_contact.address
        assert contact.homepage == prepare_link(contact_from_db.homepage)
