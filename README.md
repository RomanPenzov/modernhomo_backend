# 📘 Проект: ModernHomo Backend

## 🧠 Описание

ModernHomo — backend-сервис, созданный на FastAPI, который обрабатывает:

* регистрацию и авторизацию пользователей,
* детекцию опасных объектов или слов (Danger Events),
* транскрибацию речи,
* вычисление "индекса счастья" на основе нейросетевого анализа текста (NLP-модель).

Приложение полностью покрыто автотестами и работает с PostgreSQL через Alembic и Docker Compose.

---

## ⚙️ Технологии

* Python 3.10
* FastAPI
* PostgreSQL
* SQLAlchemy + Alembic
* Docker + Docker Compose
* Pydantic v2
* PyJWT
* HuggingFace Transformers (NLP)
* Pytest + TestClient

---

## 🗃️ Структура проекта

```
modernhomo_backend/
├── app/
│   ├── api/               # Роутеры FastAPI
│   ├── core/              # Настройки и база данных
│   ├── crud/              # CRUD-операции
│   ├── models/            # SQLAlchemy-модели
│   ├── schemas/           # Pydantic-схемы
│   ├── services/          # Логика NLP (анализ текста)
│   └── main.py            # Точка входа FastAPI
├── tests/                 # Автоматические тесты
├── migrations/            # Alembic миграции
├── docker-compose.yml     # Запуск через Docker
├── Dockerfile             # Backend образ
└── README.md              # Документация
```

---

## 🚀 Запуск проекта

### 🔧 1. Клонировать и перейти в папку проекта

```bash
git clone <repo-url>
cd modernhomo_backend
```

### 🐳 2. Запустить базу данных через Docker Compose

```bash
docker-compose up -d
```

### 📦 3. Установить зависимости в виртуальном окружении

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### ⚙️ 4. Выполнить Alembic миграции

```bash
alembic upgrade head
```

### ▶️ 5. Запустить FastAPI

```bash
uvicorn app.main:app --reload --port 8001
```

### 🧪 6. Запустить тесты

```bash
$env:PYTHONPATH = "."
pytest
```

---

## 📋 API-эндпоинты (Swagger: [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs))

| Метод | Путь              | Описание                                            |
| ----- | ----------------- | --------------------------------------------------- |
| POST  | /users/register   | Регистрация пользователя                            |
| POST  | /users/login      | Аутентификация и получение токена                   |
| GET   | /danger-events/   | Получить все события пользователя                   |
| POST  | /danger-events/   | Добавить новое событие                              |
| GET   | /transcriptions/  | Получить все транскрипции пользователя              |
| POST  | /transcriptions/  | Добавить транскрипцию                               |
| POST  | /happiness-index/ | Анализ текста (эмоции: positive, neutral, negative) |

---

## 🤖 Бизнес-логика

Модель анализа текста (`blanchefort/rubert-base-cased-sentiment`) из HuggingFace:

* получает фразу,
* возвращает эмоциональную окраску: `positive`, `neutral` или `negative`,
* используется в `/happiness-index/` и может быть расширена для дневного анализа по всем транскрибациям.

---

## 🎥 Части видео (до 7 минут)

### 🟢 Вступление:

> Здравствуйте, я разработал backend на FastAPI — это сервис ModernHomo, который выполняет авторизацию, обработку событий, транскрибации речи и анализ эмоционального состояния текста с помощью нейросети.

### 📊 База данных:

> У нас есть три связанные таблицы: `User`, `DangerEvent`, `Transcription`. Все таблицы создаются и управляются через Alembic.

### 🧪 CRUD и авторизация:

> Я покажу регистрацию пользователя, логин, получение токена и доступ к защищённым эндпоинтам `/danger-events` и `/transcriptions` через Swagger UI.

### 🧠 Бизнес-задача:

> Также реализован маршрут `/happiness-index/`, который определяет эмоциональную окраску текста. Это делается через подключённую нейросеть на HuggingFace. Например, фраза «я рад» вернёт `positive` (возможно нейронку надо будет дообучиить, так как в данный момент она применяется "как есть").

### ✅ Тесты:

> Все основные функции покрыты автоматическими тестами: регистрация, логин, события, транскрипции, анализ текста. Покрытие проверяется через pytest и TestClient.

### 🐳 Запуск:

> Приложение запускается через Docker Compose, работает с PostgreSQL, миграции выполняются Alembic, а запуск серверной части — через uvicorn.

### 🎯 Завершение:

> Таким образом, проект соответствует всем критериям: авторизация, API, бизнес-логика, миграции, тесты. Спасибо!

---

## ✅ Автор: \[Пензов Роман]
