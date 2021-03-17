from appium.webdriver.common.mobileby import MobileBy


from app_test.app_po.page.base_page import BasePage


class EditInfoPage(BasePage):
    def del_member(self):
        self.find(MobileBy.XPATH,"//*[@text='删除成员']").click()
        self.find(MobileBy.XPATH,"//*[@text='确定']").click()
