"""
Этот модуль содержит модуль danger_event.py .
Создан в рамках учебного проекта на FastAPI.
"""

# Этот файл отвечает за бизнес-логику работы с опасными событиями:
# создание событий и получение списка событий из базы данных.

from sqlalchemy.orm import Session
from app.models.danger_event import DangerEvent
from app.schemas.danger_event import DangerEventCreate

# Функция для создания нового события
def create_danger_event(db: Session, user_id: int, event: DangerEventCreate):
    """
    Создаю новое событие в базе данных, привязанное к конкретному пользователю.
    """
    db_event = DangerEvent(
        user_id=user_id,
        event_type=event.event_type,
        name=event.name,
        latitude=event.latitude,
        longitude=event.longitude
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

# Функция для получения всех событий пользователя
def get_danger_events_by_user(db: Session, user_id: int):
    """
    Получаю список всех событий, которые связаны с конкретным пользователем.
    """
    return db.query(DangerEvent).filter(DangerEvent.user_id == user_id).all()
