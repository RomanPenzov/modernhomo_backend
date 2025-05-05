# Я тестирую создание и получение событий типа DangerEvent.
# Для этого сначала регистрирую пользователя, затем получаю токен, затем отправляю события.

def get_auth_token(client, username="eventuser", password="123456"):
    """
    Вспомогательная функция: регистрирую и логиню пользователя, возвращаю токен.
    """
    client.post("/users/register", json={"username": username, "password": password})
    response = client.post("/users/login", json={"username": username, "password": password})
    return response.json()["access_token"]

def test_create_and_get_danger_event(client):
    """
    Тест создания и получения опасного события.
    """
    token = get_auth_token(client)
    headers = {"Authorization": f"Bearer {token}"}

    # Добавляю событие
    response = client.post("/danger-events/?user_id=1", headers=headers, json={
        "event_type": "object",
        "name": "нож",
        "latitude": 55.75,
        "longitude": 37.61
    })
    assert response.status_code == 200
    data = response.json()
    assert data["event_type"] == "object"
    assert data["name"] == "нож"

    # Получаю все события
    response = client.get("/danger-events/?user_id=1", headers=headers)
    assert response.status_code == 200
    event_list = response.json()
    assert len(event_list) == 1
    assert event_list[0]["name"] == "нож"
