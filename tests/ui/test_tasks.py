import allure
from playwright.sync_api import expect
from pages.tasks_page import TasksPage


@allure.feature("Управление задачами")
@allure.story("Просмотр списка задач")
def test_tasks_list_visibility(auth_page, test_config):
    tasks_page = TasksPage(auth_page)
    base_url = test_config["base_url"]

    tasks_page.open(f"{base_url}/tasks")

    tasks_page.open_sidebar_all_tasks()

    with allure.step("Проверка наличия строк в таблице задач"):
        rows = tasks_page.get_tasks_rows_locator()

        expect(rows).not_to_have_count(0, timeout=10000)
