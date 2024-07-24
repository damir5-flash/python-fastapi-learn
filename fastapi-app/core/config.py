from pydantic import BaseModel, PostgresDsn, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8001

class ApiPrefix(BaseModel):
    prefix: str = "/api"

class DatabaseSettings(BaseSettings):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=r"C:\Users\Дамир\PycharmProjects\fastApiProject3\fastapi-app\.env",  # Используем сырую строку
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP__"
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseSettings

settings = Settings()

print("DB URL:", settings.db.url)
