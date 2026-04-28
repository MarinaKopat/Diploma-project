import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import Browser
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.boards_page import BoardsPage
from pages.register_page import RegisterPage
from tests.api.api_client import ApiClient

load_dotenv()


@pytest.fixture(scope="function")
def api_admin(page, test_config):
    base_url = test_config["base_url"]
    admin_data = {
        "email": test_config["admin"][0],
        "password": test_config["admin"][1]
    }

    login_resp = page.request.post(f"{base_url}/api/auth/login", data=admin_data)
    token = login_resp.json().get("access_token")

    return ApiClient(page, base_url, token)


@pytest.fixture(scope="session")
def test_config():
    return {
        "base_url": os.getenv("BASE_URL", "http://localhost:3000"),
        "user": (os.getenv("USER_EMAIL", "user@example.com"), os.getenv("USER_PASSWORD", "password123")),
        "admin": (os.getenv("ADMIN_EMAIL", "admin@example.com"), os.getenv("ADMIN_PASSWORD", "admin123")),
    }


@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1920, "height": 1080},
        "locale": "ru-RU",
        "timezone_id": "Europe/Moscow",

    }


def perform_login(browser, base_url, credentials, storage_path):
    os.makedirs(os.path.dirname(storage_path), exist_ok=True)

    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    email, password = credentials

    login_page.open(f"{base_url}/login")
    login_page.login(email, password)

    page.wait_for_url(f"{base_url}/dashboard", timeout=60000)

    context.storage_state(path=storage_path)
    context.close()
    return storage_path


@pytest.fixture(scope="session")
def user_auth_state(browser: Browser, test_config):
    return perform_login(browser, test_config["base_url"], test_config["user"], "data/user_state.json")


@pytest.fixture(scope="session")
def admin_auth_state(browser: Browser, test_config):
    return perform_login(browser, test_config["base_url"], test_config["admin"], "data/admin_state.json")


@pytest.fixture
def auth_page(browser: Browser, user_auth_state):
    context = browser.new_context(storage_state=user_auth_state)
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def admin_page_auth(browser: Browser, admin_auth_state):
    context = browser.new_context(storage_state=admin_auth_state)
    page = context.new_page()
    yield AdminPage(page)
    context.close()


@pytest.fixture
def valid_card_data():
    return {"number": "4111 1111 1111 1111", "expiry": "12/29", "cvv": "111"}


@pytest.fixture
def declined_card_data():
    return {"number": "4000 0000 0000 0002", "expiry": "12/29", "cvv": "111"}


@pytest.fixture
def insufficient_funds_card_data():
    return {"number": "4000 0000 0000 9995", "expiry": "12/29", "cvv": "111"}


@pytest.fixture
def amex_card_data():
    return {"number": "3782 822463 10005", "expiry": "12/27", "cvv": "1225"}


@pytest.fixture
def opened_board_form(board_page):
    board_page.page.locator(board_page.CREATE_BOARD_DASHBOARD_BTN).click()
    return board_page


@pytest.fixture
def board_page(admin_page_auth, test_config):
    page_obj = BoardsPage(admin_page_auth.page)
    page_obj.open(f"{test_config['base_url']}/dashboard")
    return page_obj


@pytest.fixture
def boards_page(auth_page, test_config):
    page_obj = BoardsPage(auth_page)
    page_obj.open(f"{test_config['base_url']}/boards")
    return page_obj


@pytest.fixture
def register_page(browser, browser_context_args):
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    yield RegisterPage(page)
    context.close()
