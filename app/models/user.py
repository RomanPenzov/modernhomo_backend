# Этот файл описывает таблицу пользователей в базе данных.
# Я использую SQLAlchemy ORM для определения структуры таблицы.

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"  # Название таблицы в базе данных

    # Уникальный идентификатор пользователя
    id = Column(Integer, primary_key=True, index=True)

    # Имя пользователя (уникальное)
    username = Column(String, unique=True, index=True, nullable=False)

    # Хешированный пароль пользователя
    hashed_password = Column(String, nullable=False)

    # Отношения с другими таблицами
    danger_events = relationship("DangerEvent", back_populates="user", cascade="all, delete")
    transcriptions = relationship("Transcription", back_populates="user", cascade="all, delete")

