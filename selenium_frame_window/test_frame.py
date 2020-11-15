from selenium import webdriver
from time import sleep
# from selenium_frame_window.Base import Base

from base.Base import Base
# https://www.w3school.com.cn/tiy/t.asp?f=html_frame_cols
# https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable

class TestFrame(Base):

    def test_window(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id('droppable').text)

        self.driver.switch_to_default_content()
        print(self.driver.find_element_by_id('submitBTN').text)

