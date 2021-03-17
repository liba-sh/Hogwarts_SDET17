from appium.webdriver.common.mobileby import MobileBy

from app_test.app_po.page.base_page import BasePage

#个人信息的第二个页面
from app_test.app_po.page.editinfo_page import EditInfoPage


class PersonInfo2Page(BasePage):
    def edit_info(self):
        self.find(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        return EditInfoPage(self.driver)