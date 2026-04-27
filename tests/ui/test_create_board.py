import allure
import time
from playwright.sync_api import expect
from pages.boards_page import BoardsPage


@allure.feature("Доски")
@allure.story("Создание доски")
def test_create_board_by_admin(admin_page_auth, test_config):
    page = admin_page_auth.page
    boards_page = BoardsPage(page)
    base_url = test_config["base_url"]

    board_title = f"Auto_Board_{int(time.time())}"

    boards_page.open(f"{base_url}/dashboard")

    board_id = boards_page.create_board(board_title, "Test Description")

    with allure.step(f"Переход в доску по прямому URL: /boards/{board_id}"):
        boards_page.open(f"{base_url}/boards/{board_id}")
        page.wait_for_load_state("networkidle")

    with allure.step("Проверка заголовка созданной доски"):
        expect(page.locator(boards_page.BOARD_TITLE_H1)).to_contain_text(board_title[:15])
