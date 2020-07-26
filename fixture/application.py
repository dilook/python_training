from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("index.php"):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
