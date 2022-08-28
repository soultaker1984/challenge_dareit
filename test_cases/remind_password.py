import os
import unittest
import time
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestRemindPasswordPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_remind_password_link(self):
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/remind')
        time.sleep(3)


    @classmethod
    def tearDown(self):
        self.driver.quit()