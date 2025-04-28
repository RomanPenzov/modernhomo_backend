# Этот файл отвечает за бизнес-логику работы с транскрибациями:
# создание новых записей и получение списка транскрипций пользователя.

from sqlalchemy.orm import Session
from app.models.transcription import Transcription
from app.schemas.transcription import TranscriptionCreate

# Функция для создания новой транскрибации
def create_transcription(db: Session, user_id: int, transcription: TranscriptionCreate):
    """
    Создаю новую запись транскрибации для указанного пользователя.
    """
    db_transcription = Transcription(
        user_id=user_id,
        text=transcription.text,
        latitude=transcription.latitude,
        longitude=transcription.longitude
    )
    db.add(db_transcription)
    db.commit()
    db.refresh(db_transcription)
    return db_transcription

# Функция для получения всех транскрибаций пользователя
def get_transcriptions_by_user(db: Session, user_id: int):
    """
    Получаю все транскрибации, сделанные пользователем.
    """
    return db.query(Transcription).filter(Transcription.user_id == user_id).all()
