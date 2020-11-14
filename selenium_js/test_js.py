
from BasePage.Base import Base
import time
import pytest

class TestJs(Base):

    @pytest.mark.skip
    def test_js(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id('kw').send_keys('selenume测试')
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop = 1000")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        element = self.driver.execute_script("a = document.getElementById('train_date'); a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value = '2020-12-30'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

    

