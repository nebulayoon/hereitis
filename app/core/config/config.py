from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str


config = Settings().model_dump()
