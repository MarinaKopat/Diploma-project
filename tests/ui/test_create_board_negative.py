import allure
import pytest
from pages.boards_page import BoardsPage


@allure.feature("Доски")
@allure.story("Валидация полей")
@allure.title("Проверка валидации пустого названия")
def test_create_board_empty_name(admin_page_auth, test_config):
    page = admin_page_auth.page
    board_page = BoardsPage(page)
    base_url = test_config["base_url"]

    board_page.open(f"{base_url}/dashboard")
    board_page.open_create_modal()
    board_page.submit()

    with allure.step("Проверка сообщения для пустого поля"):
        val_msg = page.locator(board_page.TITLE_INPUT).evaluate("el => el.validationMessage")

        assert any(word in val_msg.lower() for word in ["заполните", "fill out"]), \
            f"Неожиданный текст ошибки: {val_msg}"


@allure.title("Проверка валидации минимальной длины")
@pytest.mark.parametrize("short_name, expected_len", [
    ("1", "1"),
    ("12", "2")
])
def test_create_board_min_length(admin_page_auth, test_config, short_name, expected_len):
    page = admin_page_auth.page
    board_page = BoardsPage(page)
    base_url = test_config["base_url"]

    board_page.open(f"{base_url}/dashboard")
    board_page.open_create_modal()

    board_page.fill_title(short_name)
    board_page.submit()

    with allure.step(f"Проверка ошибки для длины: {expected_len}"):
        val_msg = page.locator(board_page.TITLE_INPUT).evaluate("el => el.validationMessage")

        assert expected_len in val_msg, f"Цифра {expected_len} не найдена в ошибке: {val_msg}"
