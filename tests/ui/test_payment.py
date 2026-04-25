import allure
from playwright.sync_api import expect
from pages.payment_page import PaymentPage


@allure.feature("Оплата подписки")
class TestPayment:

    @allure.story("Успешный сценарий оплаты")
    def test_successful_payment_flow(self, page, valid_card_data):
        payment_page = PaymentPage(page)
        card = valid_card_data

        payment_page.open_payment()
        payment_page.fill_card_details(card["number"], card["expiry"], card["cvv"])
        payment_page.confirm_payment()

        with allure.step("Проверка отображения модального окна успеха"):
            expect(payment_page.success_modal).to_be_visible()
            expect(payment_page.success_title).to_have_text("Успешно!")
            expect(payment_page.success_modal).to_contain_text(card["number"][-4:])

        payment_page.make_screenshot("Successful_payment_flow")

    @allure.story("Выбор подписки и оплата картой с CVV из 4 цифр")
    @allure.title("Успешная подписка на 'Премиум' (3 месяца) через American Express")
    def test_premium_subscription_4_digit_cvv(self, page, amex_card_data):
        payment_page = PaymentPage(page)
        card = amex_card_data

        payment_page.open_payment()

        payment_page.select_period(3)
        payment_page.select_tariff("premium")

        payment_page.fill_card_details(card["number"], card["expiry"], card["cvv"])
        payment_page.confirm_payment()

        with allure.step("Проверка отображения модального окна успеха"):
            expect(payment_page.success_modal).to_be_visible(timeout=10000)
            expect(payment_page.success_title).to_have_text("Успешно!")
            expect(payment_page.success_modal).to_contain_text(card["number"][-4:])

        payment_page.make_screenshot("Premium_subscription_4_digit_cvv")

    @allure.story("Негативный сценарий: Отклонение карты")
    def test_declined_card_payment(self, page, declined_card_data):
        payment_page = PaymentPage(page)
        card = declined_card_data

        with allure.step("Открытие страницы и ввод данных отклоненной карты"):
            payment_page.open_payment()
            payment_page.fill_card_details(card["number"], card["expiry"], card["cvv"])
            payment_page.confirm_payment()

        with allure.step("Проверка появления сообщения об ошибке"):
            expect(payment_page.error_message).to_be_visible()
            expect(payment_page.error_message).to_have_text("Карта отклонена. Попробуйте другую карту")

        payment_page.make_screenshot("Declined_card_payment")

    @allure.story("Негативный сценарий: Недостаточно средств")
    def test_insufficient_funds_payment(self, page, insufficient_funds_card_data):
        payment_page = PaymentPage(page)
        card = insufficient_funds_card_data

        with allure.step("Открытие страницы и ввод данных карты с нулевым балансом"):
            payment_page.open_payment()
            payment_page.fill_card_details(card["number"], card["expiry"], card["cvv"])
            payment_page.confirm_payment()

        with allure.step("Проверка появления сообщения о недостатке средств"):
            expect(payment_page.error_message).to_be_visible()
            expect(payment_page.error_message).to_have_text("Недостаточно средств на карте")

        payment_page.make_screenshot("Insufficient_funds_payment")