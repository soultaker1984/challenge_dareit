import os
import unittest
import time
from selenium import webdriver
from pages.add_player_page import AddPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.dashboard import Dashboard


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_new_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_button()
        dashboard_page = Dashboard (self.driver)
        dashboard_page.add_player_button()
        new_player = AddPlayer(self.driver)
        new_player.type_in_name('Dimon')
        new_player.type_in_surname('Dimonium')
        new_player.type_in_age("10031994")
        new_player.type_in_main_position("Superman")
        new_player.submit_button()
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()

