import allure
from .base_page import BasePage


class AdminPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.header = page.get_by_text("Административная панель", exact=False).locator("visible=true").first

        self.ADMIN_LINK = '[data-qa="sidebar-admin-link"]'
        self.SEARCH_INPUT = 'input[data-qa="Input"]:visible'
        self.TABLE_ROWS = "tr"

    @allure.step("Открыть страницу по URL: {url}")
    def open(self, url):
        self.page.goto(url)

    @allure.step("Перейти в раздел административной панели через боковое меню")
    def open_administrative_panel(self):
        self.page.click(self.ADMIN_LINK)
        self.page.wait_for_url("**/admin")

    @allure.step("Поиск пользователя по фразе: {query}")
    def search_user(self, query):
        search_field = self.page.locator(self.SEARCH_INPUT).first

        search_field.wait_for(state="visible", timeout=10000)
        search_field.fill(query)
        search_field.press("Enter")

        self.page.wait_for_selector(self.TABLE_ROWS, state="visible", timeout=5000)

    def get_user_row(self, email: str):
        return self.page.locator(self.TABLE_ROWS).filter(has_text=email)
