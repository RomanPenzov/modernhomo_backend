"""
Этот модуль содержит модуль user.py .
Создан в рамках учебного проекта на FastAPI.
"""

# Этот файл отвечает за реализацию всех операций с пользователями в базе данных.
# Я делаю это отдельно, чтобы соблюдать принципы чистой архитектуры:
# маршруты (эндпоинты) не должны содержать бизнес-логику напрямую, всё должно быть отделено.

from sqlalchemy.orm import Session
from app.models.user import User  # Импорт модели пользователя из базы
from app.schemas.user import UserCreate  # Импорт схемы для создания нового пользователя
from passlib.context import CryptContext

# Создаю объект для хеширования паролей.
# Очень важно хранить пароли в базе не в открытом виде!
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Функция для получения пользователя по имени
def get_user_by_username(db: Session, username: str):
    """
    Ищу пользователя в базе данных по его username.
    Если пользователь найден — возвращаю объект User, иначе — None.
    """
    return db.query(User).filter(User.username == username).first()

# Функция для создания нового пользователя
def create_user(db: Session, user: UserCreate):
    """
    Создаю нового пользователя в базе данных.
    Перед сохранением пароль обязательно хешируется для безопасности.
    """
    hashed_password = pwd_context.hash(user.password)  # Хеширую пароль
    db_user = User(
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(db_user)  # Добавляю нового пользователя в сессию
    db.commit()      # Сохраняю изменения в базе
    db.refresh(db_user)  # Обновляю объект db_user из базы (чтобы получить его id)
    return db_user

# Функция для проверки пароля
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Сравниваю введённый пароль и хешированный пароль из базы данных.
    Если совпадают — возвращаю True, иначе False.
    """
    return pwd_context.verify(plain_password, hashed_password)
