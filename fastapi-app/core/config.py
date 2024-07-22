from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8001

class ApiPrefix(BaseModel):
    prefix: str ="/api"

class DatabaseSettings(BaseSettings):
    url: PostgresDsn
    echo: bool = False,
    echo_pool: bool = False,
    pool_size: int = 50,
    max_size: int = 10,

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseSettings



settings = Settings()