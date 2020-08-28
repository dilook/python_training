from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_form_contact(contact)
        wd.find_element_by_css_selector("[value=Enter]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector(f"input[value='{id}']").click()
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector("[title=Edit]")[index].click()
        self.fill_form_contact(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.edit_contact_by_id(contact.id)
        self.fill_form_contact(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def fill_form_contact(self, contact):
        self.set_field("firstname", contact.firstname)
        self.set_field("lastname", contact.lastname)
        self.set_field("middlename", contact.middlename)
        self.set_field("nickname", contact.nickname)
        self.set_field("mobile", contact.mobile_phone)
        self.set_field("work", contact.work_phone)
        self.set_field("email", contact.email)
        self.set_field("bday", contact.bday)
        self.set_field("bmonth", contact.bmonth)
        self.set_field("byear", contact.byear)
        self.set_field("company", contact.company)
        self.set_field("address", contact.address)
        self.set_field("homepage", contact.homepage)
        self.set_field("new_group", contact.new_group)
        self.set_field("title", contact.title)

    def set_field(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            if field_name in ["bday", "bmonth", "new_group"]:
                Select(wd.find_element_by_name(field_name)).select_by_value(value)
            else:
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(value)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            ll: List[WebElement] = wd.find_elements_by_name("entry")
            wd.implicitly_wait(0)
            for element in ll:
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                try:
                    homepage = cells[9].find_element_by_tag_name("a").get_attribute("origin")
                except NoSuchElementException:
                    homepage = cells[9].text
                self.contact_cache.append(
                    Contact(first_name=firstname, last_name=lastname, id=id, all_phones=all_phones,
                            address=address, all_emails=all_emails, homepage=homepage))
            wd.implicitly_wait(2)
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[56]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        homepage = wd.find_element_by_name("homepage").get_attribute("value")

        return Contact(first_name=firstname, last_name=lastname, mobile_phone=mobilephone, work_phone=workphone,
                       email=email1, address=address, homepage=homepage, id=id, home_phone=homephone,
                       secondary_phone=secondaryphone, email2=email2, email3=email3)

    def edit_contact_by_id(self, id):
        row_checkbox = self.select_contact_by_id(id)
        edit = row_checkbox.find_element_by_xpath("./../..//*[@title='Edit']")
        edit.click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        row_checkbox = wd.find_element_by_css_selector(f"input[value='{id}']")
        row_checkbox.click()
        return row_checkbox

    def add_contact_to_group(self, id, group):
        wd = self.app.wd
        self.select_contact_by_id(id)
        Select(wd.find_element_by_name("to_group")).select_by_value(group.id)
        wd.find_element_by_name("add").click()

    def filter_by_group(self, group):
        wd = self.app.wd
        self.app.open_home_page()
        Select(wd.find_element_by_name("group")).select_by_value(group.id)

