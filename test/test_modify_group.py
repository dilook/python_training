from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="MODIFIED"))
