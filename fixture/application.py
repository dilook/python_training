from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Chrome(ChromeDriverManager().install())
        self.wd.implicitly_wait(60)
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
