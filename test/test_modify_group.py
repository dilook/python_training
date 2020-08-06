from random import randrange

from model.group import Group


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="MODIFIED")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.get_id_or_max) == sorted(new_groups, key=Group.get_id_or_max)
