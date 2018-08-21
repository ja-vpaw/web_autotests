from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)

    def login(self, password, username):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("%s" % username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("%s" % password)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://192.168.111.175/")


    def destroy(self):
        self.wd.quit()
