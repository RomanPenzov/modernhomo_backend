"""Модуль описывает happiness.py . Используется в учебном проекте ModernHomo."""

# Этот файл отвечает за маршруты API для анализа эмоционального состояния текста.

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.sentiment_analyzer import analyze_sentiment

# Инициализирую роутер для работы с индексом счастья
router = APIRouter(
    prefix="/happiness-index",
    tags=["happiness-index"]
)

# Описываю схему запроса: мы ожидаем текст
class TextRequest(BaseModel):
    """
    схема запроса
    """
    text: str

# Описываю схему ответа: мы будем возвращать метку настроения
class HappinessResponse(BaseModel):
    """
    индекс счастья
    """
    sentiment: str  # Возможные значения: "positive", "neutral", "negative"

# Эндпоинт для анализа текста и определения эмоциональной окраски
@router.post("/", response_model=HappinessResponse)
def get_happiness_index(text_request: TextRequest):
    """
    Принимаю текст от пользователя, анализирую его с помощью нейросети,
    и возвращаю индекс счастья (эмоциональную метку).
    """
    sentiment = analyze_sentiment(text_request.text)
    return HappinessResponse(sentiment=sentiment)
