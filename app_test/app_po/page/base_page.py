# 基类，初始化driver,find,finds,swipe_find
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator, value):
        logging.info("find")
        logging.info(locator, value)
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        logging.info("finds")
        logging.info(locator, value)
        self.driver.find_elements(locator, value)

    def swipe_find(self, text):
        while True:
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.2
                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)
