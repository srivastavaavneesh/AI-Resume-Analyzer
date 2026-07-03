"""
Application settings.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Studio"
    APP_VERSION: str = "0.1.0"


settings = Settings()
