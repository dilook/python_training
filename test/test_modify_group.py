from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="MODIFIED"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
