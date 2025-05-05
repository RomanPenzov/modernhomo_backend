"""Модуль описывает danger_event.py . Используется в учебном проекте ModernHomo."""

# Этот файл отвечает за маршруты API для работы с событиями обнаружения объектов/слов.

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.danger_event import DangerEventCreate, DangerEventRead
from app.crud import danger_event as crud_danger_event
from app.core.database import SessionLocal

router = APIRouter(
    prefix="/danger-events",
    tags=["danger-events"]
)

# Функция для создания подключения к базе данных
def get_db():
    """
    создание подключения к базе данных.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для добавления нового события
@router.post("/", response_model=DangerEventRead)
def create_danger_event(user_id: int, event: DangerEventCreate, db: Session = Depends(get_db)):
    """
    Добавляю новое событие (объект или слово) для конкретного пользователя.
    """
    return crud_danger_event.create_danger_event(db, user_id, event)

# Эндпоинт для получения всех событий пользователя
@router.get("/", response_model=list[DangerEventRead])
def get_events(user_id: int, db: Session = Depends(get_db)):
    """
    Получаю все события для указанного пользователя.
    """
    return crud_danger_event.get_danger_events_by_user(db, user_id)
