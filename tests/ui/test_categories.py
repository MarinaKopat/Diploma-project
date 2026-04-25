import allure
from pages.categories_page import Categories
from settings.constants import BASE_URL, CARDS_URL, SUBSCRIPTION_URL, DASHBOARD_URL


@allure.feature("Навигация")
@allure.story("Открытие категорий на главной странице")
def test_open_data_cards_category(page):
    categories_page = Categories(page)
    categories_page.open(BASE_URL)

    categories_page.open_category_by_name("Карточки данных")

    categories_page.verify_url(CARDS_URL)
    categories_page.make_screenshot("Страница карточек данных")


@allure.story("Открытие категорий на главной странице")
def test_open_data_subscription_category(page):
    categories_page = Categories(page)
    categories_page.open(BASE_URL)

    categories_page.open_category_by_name("Форма подписки")

    categories_page.verify_url(SUBSCRIPTION_URL)
    categories_page.make_screenshot("Страница форма подписки")


@allure.story("Открытие категорий на главной странице")
def test_open_task_category(auth_page):
    categories_page = Categories(auth_page)
    categories_page.open(BASE_URL)

    categories_page.open_category_by_name("Система управления задачами")

    categories_page.verify_url(DASHBOARD_URL)
    categories_page.make_screenshot("Страница Система управления задачами")
