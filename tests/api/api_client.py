import allure
import json


class ApiClient:
    def __init__(self, page, base_url, token):
        self.page = page
        self.request = page.request
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}" if token else ""
        }

    def post(self, endpoint, data, expected_status=201):
        with allure.step(f"API POST {endpoint}"):
            response = self.request.post(
                f"{self.base_url}{endpoint}",
                data=json.dumps(data),
                headers=self.headers
            )
            assert response.status == expected_status, f"Got {response.status}: {response.text()}"
            return response

    def delete(self, endpoint, expected_statuses=[200, 204]):
        with allure.step(f"API DELETE {endpoint}"):
            url = f"{self.base_url}{endpoint}"
            resp = self.request.delete(url, headers=self.headers, max_redirects=0)
            if resp.status == 307:
                resp = self.request.delete(f"{url}/", headers=self.headers)
            assert resp.status in expected_statuses, f"Got {resp.status}: {resp.text()}"
            return resp

    def get(self, endpoint, expected_status=200):
        with allure.step(f"API GET {endpoint}"):
            response = self.request.get(f"{self.base_url}{endpoint}", headers=self.headers)
            assert response.status == expected_status, f"Got {response.status}: {response.text()}"
            return response
