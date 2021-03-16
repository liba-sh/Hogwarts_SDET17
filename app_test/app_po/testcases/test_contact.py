import yaml

from app_test.app_po.page.app import App


class TestContact:
    def setup(self):
        self.app=App().start()
        self.main=self.app.goto_main()

    def teardown(self):
        pass

    def test_addcontact(self):
        name="test006"
        phone="13855667706"
        editpage=self.main.goto_addressList().click_addcontact().addcontact_manual()
        editpage.edit_contact(name,phone)
        editpage.verify_ok()

    def test_delcontact(self):
        name="test005"
        phone="13855667705"
        editpage=self.main.goto_addressList().click_addcontact().addcontact_manual()
        editpage.edit_contact(name,phone)
        editpage.verify_ok()

    def test_yaml(self):
        with open("../datas/caps.yml") as f:
            datas=yaml.safe_load(f)
            print(datas)