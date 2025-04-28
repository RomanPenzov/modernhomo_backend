# Этот файл описывает схемы для событий обнаружения опасных объектов или слов.

from pydantic import BaseModel
from datetime import datetime

# Базовая схема события
class DangerEventBase(BaseModel):
    event_type: str  # Тип события: "объект" или "слово"
    name: str        # Название объекта или слова
    latitude: float  # Широта местоположения
    longitude: float # Долгота местоположения

# Схема для создания нового события
class DangerEventCreate(DangerEventBase):
    pass  # Ничего дополнительного не нужно, только базовые поля

# Схема для чтения события из базы данных
class DangerEventRead(DangerEventBase):
    id: int             # Уникальный идентификатор события
    user_id: int        # ID пользователя, связанного с событием
    timestamp: datetime # Время обнаружения события

    class Config:
        orm_mode = True  # Для поддержки работы с ORM-моделями
