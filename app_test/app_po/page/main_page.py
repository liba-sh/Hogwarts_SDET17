from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app_test.app_po.page.addresslist_page import AddressListPage
from app_test.app_po.page.base_page import BasePage


class MainPage(BasePage):
    # addressList_element = (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_addressList(self):

        # self.find(*self.addressList_element).click()
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)