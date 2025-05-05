"""
Этот модуль содержит модуля main.py.
Создан в рамках учебного проекта на FastAPI.
"""

# Импортирую FastAPI - основной фреймворк, который будет использоваться для создания REST API.
from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import user, danger_event, transcription  # Импорт моделей обязателен!
from app.api import user as user_router  # Импорт роутеров пользователей
from app.api import danger_event as danger_event_router
from app.api import transcription as transcription_router
from app.api import happiness as happiness_router

# Создаю экземпляр FastAPI-приложения
app = FastAPI(
    title="ModernHomo Backend",
    description="Сервис для получения и обработки данных от мобильного приложения ModernHomo",
    version="1.0.0"
)

# Создаю таблицы в БД при первом запуске
# Base.metadata.create_all(bind=engine) # удалил строку, т.к. теперь миграции управляют структурой базы данных, и уходим от ручного создания таблиц.

# Подключаю маршруты пользователей
app.include_router(user_router.router)
app.include_router(danger_event_router.router)
app.include_router(transcription_router.router)
app.include_router(happiness_router.router)

# Тестовый маршрут
@app.get("/")
def read_root():
    """
    Простейший тестовый эндпоинт для проверки работы сервера.
    """
    return {"message": "Добро пожаловать в API ModernHomo!"}
