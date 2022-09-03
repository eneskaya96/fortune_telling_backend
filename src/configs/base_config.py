from pydantic import BaseSettings, Field
from typing import Optional
import logging


class BaseConfig(BaseSettings):
    """Base Configuration"""

    ENVIRONMENT: Optional[str] = Field('local', env='ENVIRONMENT')

    """Secrets"""
    BROKER_URL: Optional[str]

    GRAYLOG_IP: Optional[str]
    GRAYLOG_PORT: Optional[int]

    AUTH_USERNAME: Optional[str]
    AUTH_PASSWORD: Optional[str]

    REDIS_HOST: Optional[str]
    REDIS_PORT: Optional[int]
    REDIS_PASSWORD: Optional[str]
    REDIS_DB: int = Field(0)

    """Configurations"""
    ENABLE_GRAYLOG: Optional[bool] = Field(True)
    GRAYLOG_LOGGING_LEVEL: int = Field(logging.INFO)
