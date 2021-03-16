from appium.webdriver.common.mobileby import MobileBy

from app_test.app_po.page.addcontact_page import AddContactPage
from app_test.app_po.page.base_page import BasePage


class AddressListPage(BasePage):



    def click_addcontact(self):
        element=self.swipe_find("添加成员")
        element.click()
        return AddContactPage(self.driver)
