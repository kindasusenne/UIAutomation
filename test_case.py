from selenium import webdriver
import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver import TouchActions


class Test_demo():

    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.xueersi.com/select-course")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        time.sleep(5)
        # self.driver.quit()

    @pytest.mark.skip
    def test_case_login(self):
        # $x("//*[@class='login__btn']")
        self.driver.find_element_by_xpath("//*[@class='login__btn']").click()
        self.driver.find_element_by_class_name('tab__password').click()
        self.driver.find_element_by_class_name('input-account-box').send_keys('13480855457')
        self.driver.find_element_by_class_name('input-password-box').send_keys('kindasusen0201')
        self.driver.find_element_by_class_name('login-button-content').click()

    @pytest.mark.skip
    def test_case_ActionChains_3(self):
        self.test_case_login()

        action = ActionChains(self.driver)
        touch = TouchActions()
        start_elment = self.driver.find_element_by_id('nc_1_n1z')
        # action.click_and_hold(start_elment)
        # action.click_and_hold(start_elment).release()
        action.drag_and_drop_by_offset(start_elment, 110, 0)
        action.perform()
        time.sleep(3)

    def test_case_TouchAction(self):
        # 4. 模拟按键
        self.test_case_login()
        action = ActionChains(self.driver)
        close_elemt = self.driver.find_element_by_class_name('close-btn')
        accout_elemt = self.driver.find_element_by_class_name('input-account-box')
        action.click(close_elemt)
        action.click(accout_elemt)
        action.perform()
        time.sleep(3)
        # 4. 模拟按键
        # action.send_keys(Keys.SPACE)
        action.send_keys()

