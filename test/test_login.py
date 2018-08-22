# -*- coding: utf-8 -*-

def test_success_login(app):
    wd = app.wd
    app.session.login(username="admin", password="admin")
    wd.find_element_by_xpath("//div[@id='root']/div/div/button").click()
    assert(app.wd.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='Терминал'])[1]/following::span[1]"))
    app.session.logout()


def test_unsuccess_login(app):
    wd = app.wd
    for username, password in (("admin", "adm"), ("adm", "admin")):
        print(username,password)
        app.session.login(username=username, password=password)
        wd.find_element_by_xpath("//div[@id='root']/div/div/button").click()
        assert(app.wd.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/p"))

