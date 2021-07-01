from selenium import webdriver
from selenium.webdriver.common.by import By

from ui_weixin.address_page import AddressPage


class MainPage:
    def __init__(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        # 浏览器复用
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def goto_address(self):
        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()
        return AddressPage(self.driver)

    def logout(self):
        self.driver.find_element(By.XPATH,"//*[@id='logout']").click()
