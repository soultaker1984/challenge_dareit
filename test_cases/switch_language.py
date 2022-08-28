import os
import unittest
import time
from selenium import webdriver

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestSwitchLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_switch_language(self):
        user_login = LoginPage(self.driver)
        user_login.switch_language()
        time.sleep(3)


    @classmethod
    def tearDown(self):
        self.driver.quit()