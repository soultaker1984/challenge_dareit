from pages.base_page import BasePage


class AddPlayer(BasePage):
    name_input_xpath = "//input[@name='name']"
    surname_input_xpath = "//input[@name='surname']"
    main_position_xpath = "//input[@name='mainPosition']"
    date_of_birth_xpath = "//input[@name='age']"
    submit_xpath = "//span[contains(text(),'Submit')]"

    def type_in_name(self, name):
        self.field_send_keys(self.name_input_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_input_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.date_of_birth_xpath, age)

    def type_in_main_position(self, main):
        self.field_send_keys(self.main_position_xpath, main)
    def submit_button(self):
        self.click_on_the_element(self.submit_xpath)