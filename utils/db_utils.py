import re

from model.group import Group


def clean_group_name(group_from_db):
    return Group(id=group_from_db.id, name=re.sub(' +', ' ', group_from_db.name.strip()))
