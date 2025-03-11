import pytest
import requests
import logging


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для работы с API"""

    class APIClient:
        def __init__(self, base_url):
            self.base_url = base_url
            self.session = requests.Session()
            self.logger = logging.getLogger("api_client")

        def get(self, endpoint, params=None, **kwargs):
            url = f"{self.base_url}/{endpoint}"
            self.logger.info(f"GET request to {url}")
            return self.session.get(url, params=params, **kwargs)

        def post(self, endpoint, data=None, json=None, **kwargs):
            url = f"{self.base_url}/{endpoint}"
            self.logger.info(f"POST request to {url}")
            return self.session.post(url, data=data, json=json, **kwargs)

        def put(self, endpoint, data=None, json=None, **kwargs):
            url = f"{self.base_url}/{endpoint}"
            self.logger.info(f"PUT request to {url}")
            return self.session.put(url, data=data, json=json, **kwargs)

        def patch(self, endpoint, data=None, json=None, **kwargs):
            url = f"{self.base_url}/{endpoint}"
            self.logger.info(f"PATCH request to {url}")
            return self.session.patch(url, data=data, json=json, **kwargs)

        def delete(self, endpoint, **kwargs):
            url = f"{self.base_url}/{endpoint}"
            self.logger.info(f"DELETE request to {url}")
            return self.session.delete(url, **kwargs)

    return APIClient("https://reqres.in/api")