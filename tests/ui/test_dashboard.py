import allure
from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage


@allure.feature("Панель управления")
@allure.story("Проверка статистики дашборда")
def test_dashboard_statistics(auth_page, test_config):
    dashboard = DashboardPage(auth_page)

    dashboard.open(f"{test_config['base_url']}/dashboard")

    with allure.step("Проверка корректности счетчиков статистики"):
        expect(dashboard.boards_count).not_to_have_text("0")
        expect(dashboard.total_tasks_count).not_to_have_text("0")
        expect(dashboard.in_progress_count).not_to_have_text("0")
        expect(dashboard.done_count).not_to_have_text("0")

    with allure.step("Проверка профиля и кнопок"):
        expect(dashboard.create_board_btn).to_be_visible()

        expect(dashboard.username_label).to_have_text("diana")

    dashboard.make_screenshot("Dashboard_Verification")
