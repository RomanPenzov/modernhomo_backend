"""Модуль описывает test_happiness.py . Используется в учебном проекте ModernHomo."""

# Этот тест проверяет бизнес-логику приложения:
# анализ текста и определение "индекса счастья" (эмоционального настроения).

def test_happiness_index(client):
    """
    Тест API /happiness-index/ — отправляю текст и ожидаю получить оценку настроения.
    """
    response = client.post("/happiness-index/", json={
        "text": "Я очень рад, что всё получилось!"
    })
    assert response.status_code == 200

    result = response.json()
    assert "sentiment" in result
    assert result["sentiment"] in ["positive", "neutral", "negative"]
