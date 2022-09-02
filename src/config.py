import os
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, Field, Extra

envs_dir = os.path.join(Path(__file__).parent.absolute(), 'envs')


class GlobalConfig(BaseSettings):
    """Global Configuration"""

    ENVIRONMENT: Optional[str] = Field('dev', env='ENVIRONMENT')

    DB_DRIVER: Optional[str]
    DB_HOST: Optional[str]
    DB_PASSWORD: Optional[str]
    DB_USER: Optional[str]
    DB_NAME: Optional[str]
    DB_PORT: Optional[str]
    DB_CONNECTION_URI: Optional[str]

    GRAYLOG_IP: Optional[str]
    GRAYLOG_PORT: Optional[int]
    LOG_LEVEL: Optional[str] = Field('INFO')

    AUTH_USERNAME: Optional[str]
    AUTH_PASSWORD: Optional[str]

    class Config:
        extra = Extra.allow

    def create_db_uri(self) -> str:
        self.DB_CONNECTION_URI \
            = f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return self.DB_CONNECTION_URI


class DevConfig(GlobalConfig):
    """Development Configuration"""

    class Config:
        env_file: str = os.path.join(envs_dir, 'dev.env')


class ProdConfig(GlobalConfig):
    """Production Configuration"""

    class Config:
        env_file: str = os.path.join(envs_dir, 'prod.env')


class FactoryConfig:
    """Returns a config instance depending on the ENVIRONMENT variable."""

    def __init__(self, environment: Optional[str]) -> None:
        self.environment = environment

    def __call__(self) -> GlobalConfig:
        if self.environment == "dev":
            return DevConfig()

        elif self.environment == "prod":
            return ProdConfig()

        else:
            return GlobalConfig()


class ConfigManager:
    config: GlobalConfig

    @classmethod
    def init_config(cls) -> GlobalConfig:
        cls.config = FactoryConfig(GlobalConfig().ENVIRONMENT)()
        cls.config.create_db_uri()
        return cls.config
