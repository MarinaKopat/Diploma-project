import allure
from pages.base_page import BasePage


class Categories(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.card_selector = ".feature-card"

    @allure.step("Открыть категорию '{category_name}'")
    def open_category_by_name(self, category_name: str):

        category_card = self.page.locator(self.card_selector, has_text=category_name)
        category_card.locator("a:has-text('Открыть')").click()