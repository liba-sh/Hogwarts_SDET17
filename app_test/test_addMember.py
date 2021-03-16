
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
        #跳过安装uiautomator2server等服务
        caps["skipServerInstallation"] = "true"
        #跳过设备初始化
        caps["skipDeviceInitialization"] = "true"
        # 测试之前不停止app运行
        # caps["dontStopAppOnReset"] = "true"

        #动态设置appium等待时长
        caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium服务器建立连接的代码
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def swipe_find(self,text):
        while True:
            try:
                element=self.driver.find_element(MobileBy.XPATH,f"//*[@text='{text}']")
                return element
            except:
                print("未找到")
                size=self.driver.get_window_size()
                width=size.get('width')
                height=size.get('height')
                start_x=width/2
                start_y=height*0.8
                end_x=start_x
                end_y=height*0.2
                self.driver.swipe(start_x,start_y,end_x,end_y,1000)


    def test_addMember(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        element=self.swipe_find("添加成员")
        element.click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout//*[@text='必填']").send_keys("test003")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        sleep(2)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys("13855667703")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()
        #验证添加成员toast
        #assert '添加成功' in self.driver.page_source
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成功']")

    def test_removeMember(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()

        # self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/gup']").click()
        # sleep(2)
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='test003']").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='删除成员']").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/igk").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys("test003")
        elelist=self.driver.find_elements(MobileBy.XPATH, "//*[@text='test003']")
        #find_elements方法返回的是一个列表[element1,element2...]
        if len(elelist)>1:
            elelist[1].click()
