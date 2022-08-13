from pages.base_page import BasePage


class Dashboard(BasePage):
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
    dev_team_contact_button_xpath = "//span[contains(text(),'Dev team contact')]/following-sibling::span"
    pass
