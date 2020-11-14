from selenium import webdriver
from time import sleep

class Base():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        sleep(5)
        self.driver.quit()