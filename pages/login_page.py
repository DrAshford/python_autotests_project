from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        word_in_url = 'login'
        assert word_in_url in self.browser.current_url, f'"{word_in_url}" is not presented in URL'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        email_input = self.get_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_input.send_keys(email)
        password_input = self.get_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_input.send_keys(password)
        password_input_confirm = self.get_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        password_input_confirm.send_keys(password)
        register_button = self.get_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register_button.click()