from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.__set_field_if_possible__(contact)
        wd.find_element_by_css_selector("[value=Enter]").click()
        self.app.open_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("[title=Edit]").click()
        self.__set_field_if_possible__(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()

    def __set_field_if_possible__(self, obj):
        wd = self.app.wd
        for attr, value in obj.__dict__.items():
            if value is not None:
                if attr in ["bday", "bmonth", "new_group"]:
                    Select(wd.find_element_by_name(attr)).select_by_value(value)
                else:
                    wd.find_element_by_name(attr).clear()
                    wd.find_element_by_name(attr).send_keys(value)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            td = element.find_elements_by_css_selector("td")
            lastname = td[1]
            firstname = td[2]
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(first_name=firstname, last_name=lastname, id=id))
        return contacts
