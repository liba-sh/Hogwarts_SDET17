#封装（启动app，停止app，重启app）
import yaml
from appium.webdriver import webdriver
from appium import webdriver

from app_test.app_po.page.base_page import BasePage
from app_test.app_po.page.main_page import MainPage

with open("../datas/caps.yml") as f:
    datas=yaml.safe_load(f)
    desires=datas['desirecaps']
    ip=datas['server']['ip']
    port = datas['server']['port']
class App(BasePage):
    def start(self):
        if self.driver==None:
            #启动app
            # 客户端与appium服务器建立连接的代码
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)
