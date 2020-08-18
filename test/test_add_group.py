# -*- coding: utf-8 -*-

import pytest

from data.groups import testdata
from model.group import Group


@pytest.mark.parametrize("group", testdata, ids=[repr(i) for i in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.get_id_or_max) == sorted(new_groups, key=Group.get_id_or_max)
