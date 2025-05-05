# Этот файл создает подключение к базе данных с помощью SQLAlchemy
# и содержит функцию get_db, которую я подключаю в Depends() в API и в тестах.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
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

# Эта функция подключается через Depends(get_db)
# Она открывает сессию к базе, передает в обработчик, и потом закрывает её
def get_db():
    """
    Предоставляю сессию подключения к базе данных.
    Используется во всех Depends() для работы с БД.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

