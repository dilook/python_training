import random

from model.group import Group
from utils.db_utils import clean_group_name


def test_modify_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "MODIFIED"
    app.group.modify_group(group)
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(map(clean_group_name, old_groups), key=Group.get_id_or_max) == sorted(app.group.get_group_list(),
                                                                                            key=Group.get_id_or_max)
