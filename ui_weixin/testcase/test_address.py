from time import sleep

from ui_weixin.address_page.main_page import MainPage


class TestAddress:
    def test_normal(self):
        main=MainPage()
        main.goto_address().add_member()
        sleep(6)

