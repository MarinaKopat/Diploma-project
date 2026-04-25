import allure
from playwright.sync_api import expect
from pages.tasks_page import TasksPage


@allure.feature("Управление задачами")
@allure.story("Фильтрация по статусу и приоритету")
def test_filter_tasks_by_status_and_priority(auth_page, test_config, ):
    tasks_page = TasksPage(auth_page)
    base_url = test_config["base_url"]

    tasks_page.open(f"{base_url}/tasks")

    tasks_page.open_sidebar_all_tasks()

    target_status = "В работу"
    target_priority = "Высокий"

    tasks_page.select_status(target_status)
    tasks_page.select_priority(target_priority)

    with allure.step(f"Проверка: все задачи имеют статус '{target_status}' и приоритет '{target_priority}'"):
        rows = tasks_page.get_tasks_rows_locator()

        count = rows.count()
        for i in range(count):
            row = rows.nth(i)

            status_cell = row.locator("td").nth(2)
            priority_cell = row.locator("td").nth(3)

            expect(status_cell).to_have_text(target_status, ignore_case=True)
            expect(priority_cell).to_have_text(target_priority, ignore_case=True)

    tasks_page.make_screenshot("Tasks_Filters_Success")
