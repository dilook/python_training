import random

from model.group import Group


def test_modify_some_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "MODIFIED"
    app.group.modify_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.get_id_or_max) == sorted(new_groups, key=Group.get_id_or_max)
