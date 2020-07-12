# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import configparser


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        config = configparser.ConfigParser()
        config.read("setup.ini")
        self.base_url = config['DEFAULT']['url']
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_training(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, wd):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("testGroup")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("Header")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("Footer")
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        self.return_to_groups_page(wd)

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get(self.base_url)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
