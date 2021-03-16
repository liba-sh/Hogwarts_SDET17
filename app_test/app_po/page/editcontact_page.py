from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_test.app_po.page.base_page import BasePage


class EditContactPage(BasePage):

    def edit_contact(self,name,phone):
        self.find(MobileBy.XPATH, "//android.widget.RelativeLayout//*[@text='必填']").send_keys(name)
        self.find(MobileBy.XPATH, "//*[@text='男']").click()
        sleep(2)
        self.find(MobileBy.XPATH, "//*[@text='男']").click()
        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()

    def verify_ok(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成功']")