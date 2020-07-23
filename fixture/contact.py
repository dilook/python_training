from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

        for attr, value in contact.__dict__.items():
            if value is not None:
                if attr in ["bday", "bmonth", "new_group"]:
                    Select(wd.find_element_by_name(attr)).select_by_value(value)
                else:
                    wd.find_element_by_name(attr).clear()
                    wd.find_element_by_name(attr).send_keys(value)

        wd.find_element_by_css_selector("[value=Enter]").click()

        self.app.open_home_page()
