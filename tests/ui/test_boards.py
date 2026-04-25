import allure
from playwright.sync_api import expect


@allure.feature("Управление досками")
@allure.story("Проверка списка досок пользователя")
def test_boards_elements_simplified(boards_page):
    boards_page.open_sidebar_all_boards()

    with allure.step("Проверка наличия досок в таблице"):
        rows = boards_page.get_boards_rows_locator()
        expect(rows).not_to_have_count(0, timeout=10000)
    boards_page.make_screenshot("Diana_Boards_View")
