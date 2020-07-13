# -*- coding: utf-8 -*-
import configparser
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager

from contact import Contact, ContactInfo, BDay


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        config = configparser.ConfigParser()
        config.read("setup.ini")
        self.base_url = config['DEFAULT']['url']
        self.wd = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.wd.implicitly_wait(5)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        b_day = BDay(day="1", month="April", year="1978")
        dia = Contact(first_name="Dia", middle_name="Korret", last_name="Medercy", b_day=b_day)
        dia.add_contact_info(ContactInfo(phone="+45135464151", email="test@test.com"))
        self.add_new_contact(wd, dia)
        self.open_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_new_contact(self, wd, contact):
        wd.find_element_by_link_text("add new").click()

        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("mkdia")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Dia M")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Google")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Street of Simles 23,")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("m_phone")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.contact_info.phone)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.contact_info.email)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("none")
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.b_day.day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.b_day.month)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.b_day.year)
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("[none]")
        wd.find_element_by_css_selector("[value=Enter]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
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
