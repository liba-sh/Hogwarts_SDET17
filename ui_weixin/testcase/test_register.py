from time import sleep

from ui_weixin.login_page import MainPage


class TestRegister:
    def test_register(self):
        main = MainPage()
        a = main.goto_register()
        a.register()
        sleep(6)

    def test_login_register(self):
        main = MainPage()
        a=main.goto_login()
        a.register().register()
        sleep(6)
