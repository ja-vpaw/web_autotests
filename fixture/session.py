
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, password, username):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("%s" % username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("%s" % password)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[4]/div/div").click()
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Терминал'])[1]/following::p[1]").click()
