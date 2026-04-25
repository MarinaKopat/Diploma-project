import allure
from .base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = "#id-input-login-email-input"
    PASSWORD_FIELD = "#id-input-login-password-input"
    LOGIN_BUTTON = "[data-qa='login-submit-button']"

    @allure.step("Авторизация пользователем {email}")
    def login(self, email, password):
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)