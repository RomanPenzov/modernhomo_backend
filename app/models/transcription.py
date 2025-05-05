"""
Этот модуль содержит модуль transcription.py.
Создан в рамках учебного проекта на FastAPI.
"""

# Этот файл описывает таблицу транскрибаций текста, записанных за день.

from sqlalchemy import Column, Integer, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Transcription(Base):
    """
    Это кдасс transcription.py .
    """
    __tablename__ = "transcriptions"

    id = Column(Integer, primary_key=True, index=True)

    # Внешний ключ на пользователя
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Текст транскрипции
    text = Column(Text, nullable=False)

    # Географические координаты
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Дата и время записи текста
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Обратная связь с пользователем
    user = relationship("User", back_populates="transcriptions")
