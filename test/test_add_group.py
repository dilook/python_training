# -*- coding: utf-8 -*-

from model.group import Group
from utils.db_utils import clean_group_name


def test_add_group(app, db, json_groups, check_ui):
    data_groups = json_groups
    old_groups = db.get_group_list()
    app.group.create(data_groups)
    new_groups = db.get_group_list()
    old_groups.append(data_groups)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(map(clean_group_name, old_groups), key=Group.get_id_or_max) == sorted(app.group.get_group_list(),
                                                                                            key=Group.get_id_or_max)
