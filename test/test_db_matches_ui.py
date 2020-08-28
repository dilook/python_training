from model.contact import Contact
from model.group import Group
from utils.db_utils import clean_group_name, clean_contact_name


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = map(clean_group_name, db.get_group_list())
    assert sorted(ui_list, key=Group.get_id_or_max) == sorted(db_list, key=Group.get_id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = map(clean_contact_name, db.get_contact_list())
    assert sorted(ui_list, key=Contact.get_id_or_max) == sorted(db_list, key=Contact.get_id_or_max)
