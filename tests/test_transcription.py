# Я тестирую сохранение и получение текста (транскрипций).
# Проверяю, что можно добавить запись и потом получить её обратно.

def get_auth_token(client, username="textuser", password="qwerty"):
    """
    Вспомогательная функция — регистрация и получение токена.
    """
    client.post("/users/register", json={"username": username, "password": password})
    response = client.post("/users/login", json={"username": username, "password": password})
    return response.json()["access_token"]

def test_create_and_get_transcription(client):
    """
    Тест записи транскрипции и получения списка.
    """
    token = get_auth_token(client)
    headers = {"Authorization": f"Bearer {token}"}

    # Сохраняю транскрипцию
    response = client.post("/transcriptions/?user_id=1", headers=headers, json={
        "text": "На улице спокойно.",
        "latitude": 55.75,
        "longitude": 37.61
    })
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "На улице спокойно."

    # Получаю список транскрипций
    response = client.get("/transcriptions/?user_id=1", headers=headers)
    assert response.status_code == 200
    trans = response.json()
    assert len(trans) == 1
    assert trans[0]["text"] == "На улице спокойно."
