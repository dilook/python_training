# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app, data_groups):
    old_groups = app.group.get_group_list()
    app.group.create(data_groups)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(data_groups)
    assert sorted(old_groups, key=Group.get_id_or_max) == sorted(new_groups, key=Group.get_id_or_max)
