#通讯录页面
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_test.app_po.page.addcontact_page import AddContactPage
from app_test.app_po.page.base_page import BasePage
from app_test.app_po.page.personinfo_page import PersonInfoPage


class AddressListPage(BasePage):


    #点击“添加成员”
    def click_addcontact(self):
        element=self.swipe_find("添加成员")
        element.click()
        return AddContactPage(self.driver)

    #搜索并点击一个成员，进入个人信息编辑页面
    def search_and_click(self,name):
        self.find(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/guu']").click()
        self.find(MobileBy.XPATH,"//*[@text='搜索']").send_keys(name)
        sleep(5)
        self.finds(MobileBy.XPATH, f"//*[@text='{name}']")[1].click()
        return PersonInfoPage(self.driver)

    def check_del_ok(self,name):
        self.find(MobileBy.XPATH,"//*[@text='搜索']").send_keys(name)
        sleep(5)
        eles=self.finds(MobileBy.XPATH,f"\\*[@text='{name}']")
        print(len(eles))
        # return len(eles)==1
