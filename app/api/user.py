# Этот файл отвечает за маршруты (эндпоинты) для пользователей:
# регистрация, авторизация и выдача токенов.

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead, Token
from app.crud import user as crud_user
from app.core.database import SessionLocal
from jose import jwt
from datetime import datetime, timedelta

# Инициализирую роутер для пользователей
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Секретный ключ для подписи токенов
# В реальных проектах он должен быть секретным и храниться в .env файле!
SECRET_KEY = "secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Функция для создания подключения к базе данных
def get_db():
    """
    Создаю сессию базы данных для каждого запроса.
    После запроса сессия автоматически закрывается.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для регистрации нового пользователя
@router.post("/register", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Эндпоинт для регистрации нового пользователя.
    Проверяю, нет ли уже такого пользователя в базе.
    Если всё хорошо — сохраняю пользователя и возвращаю его данные.
    """
    db_user = crud_user.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существует.")
    new_user = crud_user.create_user(db, user)
    return new_user

# Эндпоинт для авторизации пользователя и получения токена
@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    """
    Эндпоинт для входа в систему.
    Проверяю наличие пользователя и корректность пароля.
    В случае успеха — выдаю JWT-токен для последующих авторизованных запросов.
    """
    db_user = crud_user.get_user_by_username(db, username=user.username)
    if not db_user:
        raise HTTPException(status_code=400, detail="Неверное имя пользователя или пароль.")

    if not crud_user.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Неверное имя пользователя или пароль.")

    access_token = create_access_token(
        data={"sub": db_user.username}
    )

    return {"access_token": access_token, "token_type": "bearer"}

# Функция для создания JWT-токена
def create_access_token(data: dict):
    """
    Создаю токен с заданными данными.
    Устанавливаю срок действия токена.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
