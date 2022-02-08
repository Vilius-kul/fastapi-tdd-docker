import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "DEV")
    testing: bool = os.getenv("TESTING", 0)  # type: ignore
    database_url: AnyUrl = os.environ.get("DATABASE_URL")  # type: ignore


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading settings from environment...")
    return Settings()
