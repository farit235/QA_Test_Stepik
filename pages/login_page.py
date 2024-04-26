from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """
        Проверка корректности URL адреса
        """
        assert (
            self.url == "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        ), "Login URL is not correct"

    def should_be_login_form(self):
        """
        Проверка существования формы логина
        """
        assert True == BasePage.is_element_present(
            self, *LoginPageLocators.LOGIN_FORM
        ), "No login form on page"

    def should_be_register_form(self):
        """
        Проверка существования формы регистрации на странице
        """
        assert True == BasePage.is_element_present(
            self, *LoginPageLocators.REGISTRATION_FORM
        ), "No registration form on page"

    def register_new_user(self, email, password):
        """
        Функция регистрации нового пользователя
        """
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_FIELD_EMAIL
        ).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_FIELD_PASSWORD
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_FIELD_CONFIRM_PASSWORD
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.APPLY_REGISTRATION_FORM_BUTTON
        ).click()