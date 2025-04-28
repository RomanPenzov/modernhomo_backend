# Этот файл создает подключение к базе данных с помощью SQLAlchemy.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Создаю движок SQLAlchemy для подключения к базе данных
engine = create_engine(
    settings.database_url,
    echo=True  # Включаю вывод всех SQL-запросов в консоль для отладки
)

# Создаю фабрику сессий, чтобы в приложении удобно работать с базой
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаю базовый класс для всех моделей БД
Base = declarative_base()
