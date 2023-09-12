from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ConfigDict, Extra


class DatabaseSettings(BaseSettings):
    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_HOST: str = "db"  # same as container name
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "db"

    DB_URL: str = "postgresql+asyncpg://{0}:{1}@{2}:{3}/{4}"

    model_config = SettingsConfigDict(env_file='.env')


db_settings = DatabaseSettings()
