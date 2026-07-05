"""
Application configuration.

Centralizes application settings using pydantic-settings.
This module ensures that environment variables and default
values are consistently applied across the AI Resume Analyzer.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Centralized application settings.

    Responsibilities:
        - Define core application metadata (name, version).
        - Control debug mode for development vs. production.
        - Load environment variables from a `.env` file.
        - Ignore extra/unexpected environment variables safely.

    Attributes:
        app_name (str): Human-readable application name.
        app_version (str): Current version of the application.
        debug (bool): Flag to enable/disable debug mode.
    """

    app_name: str = "AI Resume Analyzer"
    app_version: str = "0.1.0"
    debug: bool = False

    primary_provider: str = "gemini"
    fallback_provider: str = "groq"

    gemini_api_key: str = ""
    groq_api_key: str = ""

    # AI Models
    gemini_model: str = "gemini-2.5-flash"
    groq_model: str = "llama-3.3-70b-versatile"

    # AI Generation
    temperature: float = 0.2
    max_tokens: int = 4096

    # Configuration for pydantic-settings
    model_config = SettingsConfigDict(
        env_file=".env",  # Load environment variables from .env file
        env_file_encoding="utf-8",  # Ensure proper encoding
        extra="ignore",  # Ignore unexpected environment variables
        case_sensitive=False,
    )


# Singleton instance for reuse across the application
settings = Settings()
