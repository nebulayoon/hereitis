from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    API_MODE: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_SECONDS: int
    REFRESH_TOKEN_EXPIRE_SECONDS: int


config = Settings()
