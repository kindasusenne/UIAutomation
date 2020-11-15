from BasePage.Base import Base
import time
import pytest
from selenium.webdriver import ActionChains


class TestAlert(Base):

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')

        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()

        time.sleep(2)
        self.driver.switch_to_alert().accept()
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id('submitBTN').click()


