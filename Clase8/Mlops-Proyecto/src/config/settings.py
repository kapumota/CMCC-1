from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # API
    app_env: str = "dev"

    # Security demo
    admin_token: str = "devtoken"

    # RAG
    docs_dir: str = "./data/docs"
    index_dir: str = "./data/indexes"
    top_k: int = 3

    # LLM (opcional)
    llm_base_url: str | None = None
    llm_api_key: str | None = None
    llm_model: str = "local-model"
    llm_temperature: float = 0.2
