from appium.webdriver.common.mobileby import MobileBy

from app_test.app_po.page.base_page import BasePage
from app_test.app_po.page.personinfo2_page import PersonInfo2Page


class PersonInfoPage(BasePage):

    #在个人信息页面上，点击右上角的更多，进入新的个人信息页面，点击“编辑成员”
    def more_info(self):
        self.find(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/guk']").click()
        return PersonInfo2Page(self.driver)