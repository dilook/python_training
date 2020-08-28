import re

from model.contact import Contact
from model.group import Group


def __strip__(string):
    return re.sub(' +', ' ', string.strip())


def clean_group_name(group_from_db):
    return Group(id=group_from_db.id, name=__strip__(group_from_db.name))


def clean_contact_name(contact_from_db):
    return Contact(id=contact_from_db.id,
                   first_name=__strip__(contact_from_db.firstname),
                   last_name=__strip__(contact_from_db.lastname))
