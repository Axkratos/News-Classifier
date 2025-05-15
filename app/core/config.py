from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import List

class Settings(BaseSettings):
    MODEL_PATH: str = "app/models/news_classifier_pipeline.pkl"
    ALLOWED_HOSTS: List[str] = ["*"]
    PORT: int = 8000

    model_config = {"env_file": ".env"}

    @field_validator("ALLOWED_HOSTS", mode="before")
    def split_hosts(cls, v):
        if isinstance(v, str):
            return [h.strip() for h in v.split(",") if h.strip()]
        return v