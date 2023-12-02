from typing import Any

from pydantic import BaseSettings, PostgresDsn

from planit.constants import Environment


class Config(BaseSettings):
    APP_VERSION: str = "1"
    ENVIRONMENT: Environment = Environment.PRODUCTION
    DATABASE_URL: PostgresDsn


settings = Config()

app_config: dict[str, Any] = {"title": "Planit API"}

if settings.ENVIRONMENT.is_deployed:
    app_config["root_path"] = f"/v{settings.APP_VERSION}"
    # Hide docs
    app_config["openapi_url"] = None