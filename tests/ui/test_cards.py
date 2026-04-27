import allure
from pages.cards_page import CardsPage
from playwright.sync_api import expect


@allure.feature("Асинхронные операции")
@allure.story("Загрузка карточек")
def test_async_cards_loading(page):
    cards_page = CardsPage(page)

    cards_page.load_cards()

    with allure.step("Проверка: карточки появились в списке"):
        expect(cards_page.cards_items).not_to_have_count(0)
