from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8001

class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

class DatabaseSettings(BaseSettings):
    url: PostgresDsn
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str , str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }


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
