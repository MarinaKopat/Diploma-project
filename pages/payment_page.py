import allure
from pages.base_page import BasePage
from settings.constants import SUBSCRIPTION_URL


class PaymentPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.card_number_input = page.get_by_test_id("card-number")
        self.expiry_input = page.locator(".card-expiry.card-input")
        self.cvv_input = page.locator(".card-cvv.card-input")
        self.pay_button = page.get_by_test_id("pay-button")
        self.success_modal = page.get_by_test_id("success-modal")
        self.success_title = page.locator(".success-title")
        self.card_last_digits = page.locator(".success-details")
        self.error_message = page.get_by_test_id("card-errors")

        self.period_1_month = page.get_by_test_id("period-1")
        self.period_3_month = page.get_by_test_id("period-3")
        self.period_12_month = page.get_by_test_id("period-12")

        self.tariff_basic = page.get_by_test_id("tariff-basic")
        self.tariff_premium = page.get_by_test_id("tariff-premium")
        self.tariff_family = page.get_by_test_id("tariff-family")

    def open_payment(self):
        self.open(SUBSCRIPTION_URL)

    @allure.step("Заполнение данных карты: {number}")
    def fill_card_details(self, number, expiry, cvv):
        self.send_keys(self.card_number_input, number)
        self.send_keys(self.expiry_input, expiry)
        self.send_keys(self.cvv_input, cvv)

    @allure.step("Подтверждение оплаты")
    def confirm_payment(self):
        self.click(self.pay_button)

    @allure.step("Выбор тарифа: {plan_type}")
    def select_tariff(self, plan_type: str):
        """plan_type: 'basic', 'premium', 'family'"""
        tariffs = {
            "basic": self.tariff_basic,
            "premium": self.tariff_premium,
            "family": self.tariff_family
        }
        self.click(tariffs[plan_type])

    @allure.step("Выбор периода: {months} мес.")
    def select_period(self, months: int):
        periods = {1: self.period_1_month, 3: self.period_3_month, 12: self.period_12_month}
        self.click(periods[months])
