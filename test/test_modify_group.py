from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group"))
    old_groups = app.group.get_group_list()
    group = Group(name="MODIFIED")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.get_id_or_max) == sorted(new_groups, key=Group.get_id_or_max)
