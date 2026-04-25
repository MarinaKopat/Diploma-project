import allure
from pages.base_page import BasePage
from settings.constants import CARDS_URL


class CardsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.load_button = page.locator("button.trigger-btn")
        self.cards_items = page.locator(".case-element")

    @allure.step("Загрузка карточек на странице")
    def load_cards(self):
        self.open(CARDS_URL)
        self.click(self.load_button)

    @allure.step("Нажать на кнопку загрузки")
    def click_load_button(self):
        self.click("button.trigger-btn")

    def get_cards_locator(self):
        return self.cards_items
