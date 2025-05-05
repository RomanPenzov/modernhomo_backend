"""
Этот модуль содержит модуль env.py.
Создан в рамках учебного проекта на FastAPI.
"""

# Я подключаю здесь свои модели и настройки окружения, чтобы Alembic мог автоматически
# создавать и применять миграции для таблиц users, danger_events, transcriptions.
# Это избавит меня от необходимости вручную пересоздавать таблицы при изменениях схемы.

import sys
import os

# Подключаю путь к корню проекта, чтобы можно было импортировать app.*
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортирую базовый класс моделей SQLAlchemy и сами модели
# Это нужно, чтобы Alembic "видел", какие таблицы нужно отслеживать
from app.core.database import Base
from app.models import user, danger_event, transcription

# Импортирую настройки подключения к БД
# Я храню их централизованно в settings, чтобы не хардкодить в alembic.ini
from app.core.config import settings

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Это объект конфигурации Alembic, который читает параметры из alembic.ini
config = context.config

# Устанавливаю переменные окружения для подключения к БД
# Использую значения из своего файла настроек (config.py)
config.set_main_option("DB_USER", settings.DB_USER)
config.set_main_option("DB_PASSWORD", settings.DB_PASSWORD)
config.set_main_option("DB_HOST", settings.DB_HOST)
config.set_main_option("DB_PORT", settings.DB_PORT)
config.set_main_option("DB_NAME", settings.DB_NAME)

# Настройка логирования Alembic (опционально)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Указываю объект metadata, чтобы Alembic знал, какие таблицы отслеживать
# Это нужно для генерации автоматических миграций
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Запускаю миграции в offline-режиме (без подключения к базе данных)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    # Начинаю транзакцию и запускаю миграции
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Запускаю миграции в online-режиме (с подключением к базе данных)."""
    # Создаю движок SQLAlchemy из настроек
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # Открываю соединение с БД и выполняю миграции
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# Определяю, как именно запускать миграции — в online или offline-режиме
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
