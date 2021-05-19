import yaml
from appium.webdriver.common.mobileby import MobileBy

from app_test.app_po.page.app import App


class TestContact:
    def setup(self):
        self.app=App().start()
        self.main=self.app.goto_main()

    def teardown(self):
        pass

    def test_addcontact(self):
        name="test001"
        phone="13855667701"
        editpage=self.main.goto_addressList().click_addcontact().addcontact_manual()
        editpage.edit_contact(name,phone)
        editpage.verify_ok()

    def test_delcontact(self):
        name="test001"
        ele=self.main.goto_addressList()
        ele.search_and_click(name).more_info().edit_info().del_member()
        # print(ele)
        # ele.find(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/gej']").click()
        # ele.check_del_ok(name)



    def test_yaml(self):
        with open("../datas/caps.yml") as f:
            datas=yaml.safe_load(f)
            print(datas)