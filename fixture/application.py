from selenium import webdriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://192.168.111.175/")

    def destroy(self):
        self.wd.quit()
