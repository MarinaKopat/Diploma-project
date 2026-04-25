import allure
from .base_page import BasePage


class RegisterPage(BasePage):
    USERNAME_INPUT = 'input[data-qa="register-username-input"]'
    EMAIL_INPUT = 'input[data-qa="register-email-input"]'
    PASSWORD_INPUT = 'input[id="id-input-register-password-input"]'
    CONFIRM_PASSWORD_INPUT = 'input[id="id-input-register-confirm-password-input"]'
    REGISTER_BTN = 'button[type="submit"]'

    def register_user(self, username, email, password):
        with allure.step(f"Регистрация пользователя: {username}"):
            self.send_keys(self.USERNAME_INPUT, username)
            self.send_keys(self.EMAIL_INPUT, email)
            self.send_keys(self.PASSWORD_INPUT, password)
            self.send_keys(self.CONFIRM_PASSWORD_INPUT, password)
            self.click(self.REGISTER_BTN)

    def get_email_validation_msg(self):
        with allure.step("Получение ошибки валидации поля Email"):
            return self.page.locator(self.EMAIL_INPUT).evaluate("el => el.validationMessage")
