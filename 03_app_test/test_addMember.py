
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "mumu_test01"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        #动态设置appium等待时长
        caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium服务器建立连接的代码
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_addMember(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout//*[@text='必填']").send_keys("test003")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        sleep(2)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys("13855667703")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()

    def test_removeMember(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/gup']").click()
        sleep(2)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='test003']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
