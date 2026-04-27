import allure
from playwright.sync_api import expect
from pages.boards_page import BoardsPage


@allure.feature("Управление досками")
@allure.story("Фильтрация досок")
def test_filter_only_public_boards(admin_page_auth, test_config):
    page = admin_page_auth.page
    boards_page = BoardsPage(page)
    base_url = test_config["base_url"]

    boards_page.open(f"{base_url}/boards")

    boards_page.filter_public_only()

    with allure.step("Проверка: в таблице только публичные доски"):
        rows = boards_page.get_boards_rows_locator()

        count = rows.count()

        for i in range(count):
            public_status_cell = rows.nth(i).locator("td").nth(2)

            expect(public_status_cell).to_have_text("Да")
