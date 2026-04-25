import allure
import time
from playwright.sync_api import expect


@allure.feature("Регистрация")
class TestRegistration:

    @allure.title("Успешная регистрация нового пользователя")
    def test_successful_registration(self, register_page, test_config):
        unique_id = int(time.time())
        username = f"user_{unique_id}"
        email = f"test_{unique_id}@example.com"
        password = "Password123!"

        register_page.open(f"{test_config['base_url']}/register")

        register_page.register_user(username, email, password)

        register_page.verify_url(f"{test_config['base_url']}/dashboard")
        with allure.step("Проверка наличия кнопки создания доски на дашборде"):
            expect(register_page.page.locator('button[data-qa="dashboard-create-board-button"]')).to_be_visible()

        register_page.make_screenshot("registration_success_final")

    @allure.title("Проверка валидации некорректного Email")
    def test_registration_invalid_email(self, register_page, test_config):
        register_page.open(f"{test_config['base_url']}/register")

        with allure.step("Заполнение формы некорректным Email"):
            register_page.send_keys(register_page.USERNAME_INPUT, "testuser")
            register_page.send_keys(register_page.EMAIL_INPUT, "invalid-email-no-at")  # Без @
            register_page.send_keys(register_page.PASSWORD_INPUT, "Password123!")
            register_page.send_keys(register_page.CONFIRM_PASSWORD_INPUT, "Password123!")

        register_page.click(register_page.REGISTER_BTN)

        error_msg = register_page.get_email_validation_msg()

        with allure.step(f"Проверка текста ошибки: {error_msg}"):
            assert "@" in error_msg or "at" in error_msg.lower()

        register_page.verify_url(f"{test_config['base_url']}/register")

        register_page.make_screenshot("invalid_email_validation")
