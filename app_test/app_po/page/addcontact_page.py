from appium.webdriver.common.mobileby import MobileBy

from app_test.app_po.page.base_page import BasePage
from app_test.app_po.page.editcontact_page import EditContactPage


class AddContactPage(BasePage):
    addContactManual=(MobileBy.XPATH,"//*[@text='手动输入添加']")
    def addcontact_manual(self):
        self.find(*self.addContactManual).click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        return EditContactPage(self.driver)