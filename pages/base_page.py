import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        with allure.step(f"Переход по адресу: {url}"):
            self.page.goto(url)

    def click(self, element_or_selector):
        with allure.step(f"Клик по элементу: {element_or_selector}"):
            if isinstance(element_or_selector, str):
                self.page.click(element_or_selector)
            else:
                element_or_selector.click()

    def send_keys(self, element_or_selector, text):
        with allure.step(f"Ввод текста '{text}' в {element_or_selector}"):
            if isinstance(element_or_selector, str):
                self.page.fill(element_or_selector, text)
            else:
                element_or_selector.fill(text)

    def press_key(self, key: str):
        with allure.step(f"Нажатие клавиши: {key}"):
            self.page.keyboard.press(key)

    def verify_url(self, expected_url: str):
        with allure.step(f"Проверка перехода на {expected_url}"):
            expect(self.page).to_have_url(expected_url)

    def make_screenshot(self, name="Screenshot"):
        with allure.step(f"Снятие скриншота: {name}"):
            allure.attach(
                self.page.screenshot(full_page=True),
                name=name,
                attachment_type=allure.attachment_type.PNG
            )

    def reload(self):
        with allure.step("Обновление страницы"):
            self.page.reload(wait_until="networkidle")