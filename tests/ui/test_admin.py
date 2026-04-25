import allure
from playwright.sync_api import expect
from pages.admin_page import AdminPage


@allure.feature("Админ-панель")
class TestAdminAccess:
    @allure.title("Мгновенная проверка доступа админа")
    def test_admin_access_fast(self, admin_page_auth, test_config):
        admin_url = f"{test_config['base_url']}/admin"

        with allure.step(f"Переход по прямой ссылке в админку: {admin_url}"):
            admin_page_auth.open(admin_url)

        with allure.step("Проверка: заголовок админки отображается"):
            expect(admin_page_auth.header).to_be_visible(timeout=10000)
            admin_page_auth.make_screenshot("Admin_Access_Success")

    @allure.title("Запрет доступа для обычного пользователя")
    def test_non_admin_denied(self, auth_page, test_config):
        admin_page = AdminPage(auth_page)
        admin_url = f"{test_config['base_url']}/admin"

        with allure.step(f"Попытка неавторизованного перехода в админку: {admin_url}"):
            admin_page.open(admin_url)

        with allure.step("Проверка: заголовок админки НЕ виден"):
            expect(admin_page.header).not_to_be_visible()
            admin_page.make_screenshot("Non_Admin_Denied_Result")
