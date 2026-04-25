import allure
import time
from playwright.sync_api import expect


@allure.feature("API Доски")
def test_create_and_delete_board_via_api(api_admin, page, test_config):
    board_title = f"API_Board_{int(time.time())}"

    resp = api_admin.post("/api/boards/", {
        "title": board_title,
        "description": "Clean test",
        "public": True
    })
    board_id = resp.json()["id"]

    api_admin.delete(f"/api/boards/{board_id}")

    api_admin.get(f"/api/boards/{board_id}", expected_status=404)
    page.goto(f"{test_config['base_url']}/dashboard")
    expect(page.get_by_text(board_title)).not_to_be_visible()
