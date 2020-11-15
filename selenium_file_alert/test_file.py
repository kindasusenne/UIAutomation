from base.Base import Base
import time
import pytest


class TestFile(Base):

    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("stfile").send_keys("D:\\02-PythonProject\\UIAutomation\\image\\OIP.jpg")
        time.sleep(5)



