from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@name='password']"
    sign_in_button_xpath = "//span[contains(@class,'MuiButton')]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = "Scouts panel - sign in"
    header_text_xpath = "//h5[text()='Scouts Panel']"
    header_text = 'Scouts Panel'


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_on_the_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
    def check_the_text_of_the_box(self):
        self.assert_element_text(self.driver, self.header_text_xpath, self.header_text)
