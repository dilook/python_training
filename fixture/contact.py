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
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("[title=Edit]").click()
        self.fill_form_contact(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def fill_form_contact(self, contact):
        self.set_field("firstname", contact.firstname)
        self.set_field("lastname", contact.lastname)
        self.set_field("middlename", contact.middlename)
        self.set_field("nickname", contact.nickname)
        self.set_field("mobile", contact.mobile)
        self.set_field("work", contact.work)
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
            for element in wd.find_elements_by_name("entry"):
                td = element.find_elements_by_css_selector("td")
                lastname = td[1].text
                firstname = td[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=firstname, last_name=lastname, id=id))
        return list(self.contact_cache)
