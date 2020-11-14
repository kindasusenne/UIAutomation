from selenium import webdriver
import time
from selenium.webdriver import ActionChains

class Test_demo():

    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.xueersi.com/select-course")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_case_login(self):
        # $x("//*[@class='login__btn']")
        self.driver.find_element_by_xpath("//*[@class='login__btn']").click()
        self.driver.find_element_by_class_name('tab__password').click()
        self.driver.find_element_by_class_name('input-account-box').send_keys('13480855457')
        self.driver.find_element_by_class_name('input-password-box').send_keys('kindasusen0201')
        self.driver.find_element_by_class_name('login-button-content').click()

        action = ActionChains(self.driver)
        start_elment = self.driver.find_element_by_id('nc_1_n1z')
        action.click_and_hold(start_elment)
        action.drag_and_drop_by_offset(start_elment,100,0)
        action.perform()
        time.sleep(3)


