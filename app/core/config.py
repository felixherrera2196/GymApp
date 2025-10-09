"""Application configuration module."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = "GymApp"
    api_version: str = "v1"

    class Config:
        env_file = ".env"
        case_sensitive = True


def get_settings() -> Settings:
    """Return cached application settings instance."""
    return Settings()
