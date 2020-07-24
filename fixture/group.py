class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.__set_field_if_possible__(group)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        self.open_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.__set_field_if_possible__(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def __set_field_if_possible__(self, obj):
        wd = self.app.wd
        for attr, value in obj.__dict__.items():
            if value is not None:
                wd.find_element_by_name(f"group_{attr}").clear()
                wd.find_element_by_name(f"group_{attr}").send_keys(value)
