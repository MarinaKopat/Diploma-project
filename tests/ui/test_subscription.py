import allure
from playwright.sync_api import expect
from pages.subscription_page import SubscriptionPage


@allure.feature("Subscription Page")
class TestSubscription:

    @allure.story("Позитивный сценарий")
    @allure.title("Успешное применение промокода ALWAYS")
    def test_promo_activation_success(self, page):
        subscription_page = SubscriptionPage(page)

        subscription_page.open_subscription()
        subscription_page.apply_promo("ALWAYS")

        with allure.step("Проверка сообщения об успехе"):
            expect(subscription_page.success_message).to_be_visible()
            expect(subscription_page.success_message).to_have_text(
                "Промокод применён: Скидка 15% для для всех тарифов"
            )
            subscription_page.make_screenshot("Promo_activation")

    @allure.story("Позитивный сценарий")
    @allure.title("Проверка спеццены 199$ в корзине после промокода BASIC199")
    def test_promo_updates_final_price(self, page):
        subscription_page = SubscriptionPage(page)

        subscription_page.open_subscription()

        with allure.step("Выбор Базового тарифа"):
            subscription_page.basic_tariff_card.click()

            subscription_page.apply_promo("BASIC199")

            with allure.step("Проверка сообщения о применении"):
                expect(subscription_page.success_message).to_be_visible()
                expect(subscription_page.success_message).to_contain_text(
                    "Промокод применён: Специальная цена 199₷/мес на Базовый тариф"
                )

            with allure.step("Проверка изменения итоговой цены на кнопке"):
                expect(subscription_page.checkout_button).to_contain_text("1 911₷")

                subscription_page.make_screenshot("Promo_updates_final_price")

    @allure.story("Негативный сценарий")
    @allure.title("Ошибка при вводе невалидного промокода")
    def test_promo_activation_error(self, page):
        subscription_page = SubscriptionPage(page)

        subscription_page.open_subscription()
        subscription_page.apply_promo("WELCOME10")

        with allure.step("Проверка появления сообщения об ошибке"):
            expect(subscription_page.error_message).to_be_visible()
            expect(subscription_page.error_message).to_contain_text("Промокод истек")

            subscription_page.make_screenshot("Promo_activation_error")
