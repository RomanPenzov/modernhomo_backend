"""
Этот модуль содержит модуль danger_event.py.
Создан в рамках учебного проекта на FastAPI.
"""

# Этот файл описывает таблицу опасных событий (объекты и слова).

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class DangerEvent(Base):
    """
    Это класс DangerEvent.
    """
    __tablename__ = "danger_events"

    id = Column(Integer, primary_key=True, index=True)

    # Внешний ключ на пользователя
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Тип события: "объект" или "слово"
    event_type = Column(String, nullable=False)

    # Название обнаруженного объекта или слова
    name = Column(String, nullable=False)

    # Географические координаты
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Дата и время события
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Обратная связь с пользователем
    user = relationship("User", back_populates="danger_events")
