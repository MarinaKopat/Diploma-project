import allure
import time
from playwright.sync_api import expect
from tests.api.utils_helpers import get_user_id_from_jwt


@allure.feature("API Администрирование")
@allure.story("Удаление пользователя")
def test_admin_deletes_user_api(api_admin, admin_page_auth, test_config):
    unique_id = int(time.time())
    username = f"api_user_{unique_id}"

    with allure.step("Регистрация нового пользователя"):
        payload = {
            "username": username,
            "email": f"api_{unique_id}@example.com",
            "password": "Password123!",
            "password_confirm": "Password123!"
        }

        reg_resp = api_admin.post("/api/auth/register", data=payload)
        user_id = get_user_id_from_jwt(reg_resp.json().get("access_token"))
        assert user_id is not None

    with allure.step(f"Удаление пользователя ID {user_id}"):
        api_admin.delete(f"/api/users/{user_id}")

    with allure.step("Визуальная проверка в админ-панели"):
        page = admin_page_auth.page
        page.goto(f"{test_config['base_url']}/admin")
        page.wait_for_load_state("networkidle")

        expect(page.get_by_text(username)).not_to_be_visible()

        allure.attach(
            page.screenshot(full_page=True),
            name="admin_panel_final",
            attachment_type=allure.attachment_type.PNG
        )
