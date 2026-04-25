import allure
from .base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.boards_count = page.locator('[data-qa="dashboard-stat-total-boards-value"]')
        self.total_tasks_count = page.locator('[data-qa="dashboard-stat-total-tasks-value"]')
        self.in_progress_count = page.locator('[data-qa="dashboard-stat-in-progress-value"]')
        self.done_count = page.locator('[data-qa="dashboard-stat-done-value"]')
        self.create_board_btn = page.locator('[data-qa="dashboard-create-board-button"]')
        self.username_label = page.locator(".header-username")

    @allure.step("Нажать кнопку создания новой доски")
    def click_create_board(self):
        self.click(self.create_board_btn)

    @allure.step("Получить имя текущего пользователя")
    def get_logged_in_username(self):
        return self.username_label.inner_text()