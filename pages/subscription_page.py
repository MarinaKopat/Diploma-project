import allure
from pages.base_page import BasePage
from settings.constants import SUBSCRIPTION_URL


class SubscriptionPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.promo_input = page.locator(".promo-input-wrapper input")
        self.success_message = page.get_by_test_id("promo-message")
        self.error_message = page.locator(".promo-message.error")
        self.basic_tariff_card = page.get_by_test_id("tariff-basic")
        self.checkout_button = page.get_by_test_id("pay-button")
        self.total_price_display = page.locator(".total-price-section")

    def open_subscription(self):
        self.open(SUBSCRIPTION_URL)
        self.promo_input.wait_for(state="visible")

    def apply_promo(self, code: str):
        self.send_keys(self.promo_input, code)
        self.promo_input.press("Enter")

    def select_basic_tariff(self):
        with allure.step("Выбор базового тарифа"):
            self.click(self.basic_tariff_card)
