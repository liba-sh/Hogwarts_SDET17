from selenium import webdriver
from selenium.webdriver.common.by import By

from ui_weixin.login_page.login_page import LoginPage
from ui_weixin.login_page.register_page import RegisterPage


class MainPage:
    def __init__(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        # 浏览器复用
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_head_info_pCDownloadBtn']").click()
        return RegisterPage(self.driver)

    def goto_login(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        return LoginPage(self.driver)
