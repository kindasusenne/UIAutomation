from selenium import webdriver
from time import sleep
import os

class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver=webdriver.firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        sleep(5)
        self.driver.quit()