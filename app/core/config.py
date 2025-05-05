# Этот файл отвечает за хранение всех настроек проекта, чтобы удобно обращаться к ним из разных частей кода.
# Храню такие вещи отдельно, чтобы избежать хардкода параметров прямо в коде.

from pydantic_settings import BaseSettings

# Определяю класс настроек через BaseSettings, чтобы автоматически загружать параметры окружения.
class Settings(BaseSettings):
    """
    класс настроек через BaseSettings, чтобы автоматически загружать параметры окружения.
    """
    # Настройки подключения к базе данных PostgreSQL
    DB_USER: str = "modernhomo_user"
    DB_PASSWORD: str = "modernhomo_password"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "modernhomo_db"

    # Специальное свойство для сборки строки подключения
    @property
    def database_url(self):
        """
        Генерирует URL подключения к базе данных PostgreSQL в формате,
        который понимает SQLAlchemy.
        """
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

# Создаю экземпляр настроек, который буду использовать по всему проекту
settings = Settings()
