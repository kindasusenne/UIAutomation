from selenium import webdriver
from time import sleep
import pytest
from base.Base import Base
class TestWindows(Base):

    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        sleep(3)
        self.driver.find_element_by_link_text("立即注册").click()
        sleep(3)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('16675357538')
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('userpassword')

        self.driver.switch_to_window(windows[0])
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('userpassword')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()




