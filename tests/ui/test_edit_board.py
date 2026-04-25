import allure
import time
from playwright.sync_api import expect
from pages.boards_page import BoardsPage


@allure.feature("Управление досками")
@allure.story("Универсальное редактирование")
def test_admin_edits_first_available_board(admin_page_auth, test_config):
    page = admin_page_auth.page
    boards_page = BoardsPage(page)
    base_url = test_config["base_url"]

    boards_page.open(f"{base_url}/boards")

    boards_page.open_first_board()

    new_title = f"Auto_Updated_{int(time.time())}"
    boards_page.edit_board_title(new_title)

    with allure.step("Проверка обновления заголовка"):
        expect(page.locator(boards_page.BOARD_TITLE_H1)).to_contain_text(new_title[:15])
        boards_page.make_screenshot("Final_Edit_Result")
