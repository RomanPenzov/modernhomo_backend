# Этот файл содержит фикстуры для запуска тестов: создаю тестовую БД,
# использую специальную тестовую сессию SQLAlchemy, и подменяю зависимость get_db.

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base
from app.main import app
from app.core.config import settings

# Я создаю тестовую БД PostgreSQL (отдельную от основной).
# Можно использовать SQLite для простоты, но я показываю вариант с PostgreSQL через Docker (по учебному заданию).

# Подключение к той же БД, но можно указать имя базы modernhomo_test, если создать отдельную БД
SQLALCHEMY_TEST_DATABASE_URL = settings.database_url

# Создаю движок SQLAlchemy для тестовой БД
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)

# Создаю тестовую сессию SQLAlchemy
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Эта фикстура автоматически вызывается перед каждым тестом
# Я создаю все таблицы, затем удаляю — чтобы тесты не мешали друг другу
@pytest.fixture(scope="function")
def db():
    """
    Фикстура тестовой БД: создаёт таблицы перед тестом, удаляет после теста.
    """
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

# Подменяю зависимость get_db внутри приложения, чтобы использовать тестовую сессию
@pytest.fixture(scope="function")
def client(db):
    """
    Тестовый клиент FastAPI, использующий тестовую БД.
    """
    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[settings.get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
