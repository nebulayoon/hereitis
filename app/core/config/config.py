from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    API_MODE: str


config = Settings()
