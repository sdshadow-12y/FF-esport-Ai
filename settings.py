import os
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    openai_api_key: str = ""
    openai_model: str = "gpt-4.1-mini"
    app_env: str = "development"
    frontend_origins: list[str] = ["http://localhost:5500", "http://127.0.0.1:5500"]
    firebase_service_account_path: str = ""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", case_sensitive=False)
settings = Settings()
