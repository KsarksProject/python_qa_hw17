from jsonschema import validate
from schemas.resources import resource_schema


class TestResourcesAPI:
    """Тесты для проверки работы с ресурсами API reqres.in"""

    def test_get_existing_resource(self, api_client):
        """✅ Проверка получения информации о существующем ресурсе"""
        resource_id = 2
        response = api_client.get(f"unknown/{resource_id}")

        assert response.status_code == 200
        body = response.json()
        validate(body, resource_schema)
        assert body["data"]["id"] == resource_id

    def test_get_non_existing_resource(self, api_client):
        """✅ Проверка получения информации о несуществующем ресурсе"""
        response = api_client.get("unknown/56")

        assert response.status_code == 404
        assert response.json() == {}
