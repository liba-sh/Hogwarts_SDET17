from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self, driver):
        self.driver = driver

    def add_member(self):
        def wait_name(driver):
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_name)
        a=self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
        a[-1].click()
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("test002")
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("5678")
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("15105671235")
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()
