# Этот файл описывает схемы для текстов, которые были транскрибированы за день.

from pydantic import BaseModel
from datetime import datetime

# Базовая схема для транскрибации
class TranscriptionBase(BaseModel):
    text: str           # Сам текст транскрибации
    latitude: float     # Широта местоположения
    longitude: float    # Долгота местоположения

# Схема для создания новой записи транскрибации
class TranscriptionCreate(TranscriptionBase):
    pass  # Ничего дополнительно не требуется

# Схема для ответа клиенту после записи/получения ттранскрибации
class TranscriptionRead(TranscriptionBase):
    id: int             # Уникальный идентификатор транскрибации
    user_id: int        # ID пользователя
    timestamp: datetime # Дата и время записи текста

    class Config:
        orm_mode = True  # Поддержка работы с ORM
