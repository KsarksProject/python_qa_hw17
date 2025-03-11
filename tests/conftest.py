import pytest
import requests


@pytest.fixture
def api_client():
    """Фикстура для HTTP-клиента"""
    base_url = "https://reqres.in/api/"

    class APIClient:
        def get(self, endpoint):
            return requests.get(base_url + endpoint)

        def post(self, endpoint, json=None):
            return requests.post(base_url + endpoint, json=json)

        def put(self, endpoint, json=None):
            return requests.put(base_url + endpoint, json=json)

        def patch(self, endpoint, json=None):
            return requests.patch(base_url + endpoint, json=json)

        def delete(self, endpoint):
            return requests.delete(base_url + endpoint)

    return APIClient()
