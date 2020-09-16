# -*- coding: utf-8 -*-
import allure

from model.group import Group
from utils.db_utils import clean_group_name


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step("I add the group %s to the list" % group):
        app.group.create(group)
    with allure.step("the new group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(map(clean_group_name, old_groups), key=Group.get_id_or_max) == sorted(app.group.get_group_list(),
                                                                                                key=Group.get_id_or_max)
