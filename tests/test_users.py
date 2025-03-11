from jsonschema import validate
from schemas import users


class TestUsersAPI:
    """Тесты для проверки работы с пользователями API reqres.in"""

    def test_create_user_success(self, api_client):
        """✅ Проверка успешного создания пользователя"""
        user_data = {"name": "morpheus", "job": "leader"}
        response = api_client.post("users", json=user_data)

        assert response.status_code == 201
        body = response.json()
        validate(body, users.post_user)
        assert body["name"] == user_data["name"]
        assert body["job"] == user_data["job"]
        assert "id" in body
        assert "createdAt" in body

    def test_get_existing_user(self, api_client):
        """✅ Проверка получения информации о существующем пользователе"""
        user_id = 2
        response = api_client.get(f"users/{user_id}")

        assert response.status_code == 200
        body = response.json()
        validate(body, users.get_user)
        assert body["data"]["id"] == user_id

    def test_get_non_existing_user(self, api_client):
        """✅ Проверка получения информации о несуществующем пользователе"""
        response = api_client.get("users/56")

        assert response.status_code == 404
        assert response.json() == {}

    def test_full_user_update(self, api_client):
        """✅ Проверка полного обновления информации о пользователе (PUT)"""
        user_id = 2
        user_data = {"name": "John Deer", "job": "tractor"}
        response = api_client.put(f"users/{user_id}", json=user_data)

        assert response.status_code == 200
        body = response.json()
        validate(body, users.update_user)
        assert body["name"] == user_data["name"]
        assert body["job"] == user_data["job"]
        assert "updatedAt" in body

    def test_partial_user_update(self, api_client):
        """✅ Проверка частичного обновления информации о пользователе (PATCH)"""
        user_id = 2
        user_data = {"name": "Neo"}
        response = api_client.patch(f"users/{user_id}", json=user_data)

        assert response.status_code == 200
        body = response.json()
        validate(body, users.update_user)
        assert body["name"] == user_data["name"]
        assert "updatedAt" in body

    def test_successful_user_registration(self, api_client):
        """✅ Проверка успешной регистрации пользователя"""
        user_data = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = api_client.post("register", json=user_data)

        assert response.status_code == 200
        body = response.json()
        validate(body, users.register_user)
        assert "id" in body
        assert "token" in body

    def test_unsuccessful_user_registration(self, api_client):
        """✅ Проверка неуспешной регистрации пользователя (без пароля)"""
        user_data = {"email": "master@flomaster"}
        response = api_client.post("register", json=user_data)

        assert response.status_code == 400
        body = response.json()
        validate(body, users.error_register_user)
        assert "error" in body

    def test_delete_existing_user(self, api_client):
        """✅ Проверка удаления существующего пользователя"""
        user_id = 2
        response = api_client.delete(f"users/{user_id}")

        assert response.status_code == 204
        assert response.text == ""
