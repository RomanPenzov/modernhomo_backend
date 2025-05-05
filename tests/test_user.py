# Этот файл содержит автоматические тесты на регистрацию, логин и доступ к защищённому эндпоинту.

def test_register_user(client):
    """
    Тест регистрации нового пользователя.
    Проверяю, что API возвращает статус 200 и ID пользователя.
    """
    response = client.post("/users/register", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["username"] == "testuser"

def test_login_user(client):
    """
    Тест логина пользователя и получения токена.
    Сначала регистрирую пользователя, затем проверяю выдачу токена.
    """
    client.post("/users/register", json={
        "username": "testuser2",
        "password": "testpass"
    })
    response = client.post("/users/login", json={
        "username": "testuser2",
        "password": "testpass"
    })
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
