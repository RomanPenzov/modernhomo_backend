"""Модуль описывает transcription.py. Используется в учебном проекте ModernHomo."""

# Этот файл отвечает за маршруты API для работы с транскрибациями текста.

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.transcription import TranscriptionCreate, TranscriptionRead
from app.crud import transcription as crud_transcription
from app.core.database import SessionLocal

router = APIRouter(
    prefix="/transcriptions",
    tags=["transcriptions"]
)

# Функция для создания подключения к базе данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для добавления новой транскрибации
@router.post("/", response_model=TranscriptionRead)
def create_transcription(user_id: int, transcription: TranscriptionCreate, db: Session = Depends(get_db)):
    """
    Добавляю новую запись транскрибации для пользователя.
    """
    return crud_transcription.create_transcription(db, user_id, transcription)

# Эндпоинт для получения всех транскрибаций пользователя
@router.get("/", response_model=list[TranscriptionRead])
def get_transcriptions(user_id: int, db: Session = Depends(get_db)):
    """
    Получаю все транскрибации указанного пользователя.
    """
    return crud_transcription.get_transcriptions_by_user(db, user_id)
