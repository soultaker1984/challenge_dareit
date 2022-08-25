from pages.base_page import BasePage
import time


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl'
    header_xpath = "//header"
    scouts_panel_header_xpath = "//h6[text()='Scouts Panel']"
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//*[text()='Players']"
    Polski_xpath = "//*[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    players_count_words_xpath = "//div[text()='Players count']"
    number_of_players_xpath = "//*[text()='10']"
    add_player_button_xpath = "//span[text()='Add player']"
    shortcuts_xpath = "//h2[text()='Shortcuts']"
    dev_team_contact_label_xpath = "//span[contains(text(),'Dev team contact')]"
    dev_team_contact_button_xpath = "//span[contain"
    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
