import allure
from .base_page import BasePage


class TasksPage(BasePage):
    SIDEBAR_TASKS = '[data-qa="sidebar-tasks-link"]'
    TASKS_TABLE_ROWS = "table tbody tr"

    STATUS_SELECT = '[data-qa="tasks-status-filter"]'
    PRIORITY_SELECT = '[data-qa="tasks-priority-filter"]'

    @allure.step("Открыть все задачи через сайдбар")
    def open_sidebar_all_tasks(self):
        self.click(self.SIDEBAR_TASKS)
        self.page.wait_for_load_state("networkidle")

    @allure.step("Установить фильтр статуса: '{status}'")
    def select_status(self, status: str):
        # select_option работает со стандартными тегами <select>
        self.page.select_option(self.STATUS_SELECT, label=status)
        self.page.wait_for_load_state("networkidle")

    @allure.step("Установить фильтр приоритета: '{priority}'")
    def select_priority(self, priority: str):
        self.page.select_option(self.PRIORITY_SELECT, label=priority)
        self.page.wait_for_load_state("networkidle")

    @allure.step("Получить локатор строк таблицы задач")
    def get_tasks_rows_locator(self):
        return self.page.locator(self.TASKS_TABLE_ROWS)


