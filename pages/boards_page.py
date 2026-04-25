import allure
from .base_page import BasePage


class BoardsPage(BasePage):
    SIDEBAR_BOARDS = '[data-qa="sidebar-boards-link"]'
    BOARDS_TABLE_ROWS = "table tbody tr"
    OPEN_BOARD_LINK = 'text="Открыть"'

    BOARD_TITLE_H1 = '[data-qa="board-title"]'
    EDIT_BOARD_BTN = '[data-qa="board-edit-button"]'
    MODAL_TITLE_INPUT = '[data-qa="edit-board-title-input"]'
    MODAL_SAVE_BTN = '[data-qa="edit-board-save-button"]'
    PUBLIC_ONLY_CHECKBOX = '[data-qa="boards-public-only-checkbox"]'
    CREATE_BOARD_DASHBOARD_BTN = 'button[data-qa="dashboard-create-board-button"]'
    TITLE_INPUT = 'input[data-qa="create-board-title-input"]'
    DESCRIPTION_TEXTAREA = 'textarea[data-qa="create-board-description-textarea"]'
    PUBLIC_CHECKBOX = 'input[data-qa="create-board-public-checkbox"]'
    SUBMIT_BTN = 'button[data-qa="create-board-submit-button"]'

    @allure.step("Открыть все доски через сайдбар")
    def open_sidebar_all_boards(self):
        self.page.click(self.SIDEBAR_BOARDS)

    @allure.step("Получить локатор строк таблицы досок")
    def get_boards_rows_locator(self):
        return self.page.locator(self.BOARDS_TABLE_ROWS)

    @allure.step("Открыть первую доску из списка")
    def open_first_board(self):
        first_row = self.page.locator(self.BOARDS_TABLE_ROWS).first
        first_row.wait_for(state="visible")
        self.click(first_row.locator(self.OPEN_BOARD_LINK))
        self.page.wait_for_load_state("networkidle")

    @allure.step("Редактировать название доски на '{new_title}'")
    def edit_board_title(self, new_title: str):
        self.click(self.EDIT_BOARD_BTN)
        self.send_keys(self.MODAL_TITLE_INPUT, new_title)
        self.click(self.MODAL_SAVE_BTN)
        self.page.wait_for_load_state("networkidle")

    @allure.step("Установить фильтр 'Только публичные'")
    def filter_public_only(self):
        self.click(self.PUBLIC_ONLY_CHECKBOX)
        self.page.wait_for_load_state("networkidle")

    def create_board(self, title: str, description: str):
        with allure.step(f"Создание доски: {title}"):
            self.click(self.CREATE_BOARD_DASHBOARD_BTN)
            self.send_keys(self.TITLE_INPUT, title)
            self.send_keys(self.DESCRIPTION_TEXTAREA, description)
            self.page.locator(self.PUBLIC_CHECKBOX).set_checked(True, force=True)

            with self.page.expect_response("**/api/boards/") as response_info:
                self.click(self.SUBMIT_BTN)

            resp = response_info.value
            board_id = resp.json().get('id')
            self.page.locator(self.SUBMIT_BTN).wait_for(state="hidden", timeout=10000)
            return board_id

    def get_error_locator(self, text_pattern: str):
        return self.page.get_by_text(text_pattern, exact=False)

    def open_create_modal(self):
        with allure.step("Открыть модальное окно создания доски"):
            self.click(self.CREATE_BOARD_DASHBOARD_BTN)

    def fill_title(self, text: str):
        with allure.step(f"Ввести название: {text}"):
            self.send_keys(self.TITLE_INPUT, text)

    def submit(self):
        with allure.step("Нажать кнопку создания"):
            self.click(self.SUBMIT_BTN)
