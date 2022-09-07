import os
from pathlib import Path
from pydantic import Field, Extra
from typing import Optional
from src.configs.base_config import BaseConfig

envs_dir = os.path.join(Path(__file__).parent.parent.parent.absolute(), 'envs')


class GlobalConfig(BaseConfig):
    """Global Configuration"""

    """Secrets"""
    FORTUNE_API_URL: Optional[str]
    BROKER_URL: Optional[str]

    """Configurations"""
    WORKER_CONCURRENCY: int = Field(1)

    FORTUNE_API_READ_TIMEOUT: float = Field(4.0)
    FORTUNE_API_NUMBER_OF_RETRIES: int = Field(1)
    FORTUNE_API_CONNECT_TIMEOUT: float = Field(1.0)

    BEAT_CREATE_FORTUNE_INTERVAL: int = Field(1)
    EXPIRE_TIME_OF_TASKS: int = Field(600, env='EXPIRE_TIME_OF_TASKS')

    class Config:
        extra = Extra.allow


class LocalConfig(GlobalConfig):
    """Local Configuration"""

    class Config:
        env_file: str = os.path.join(envs_dir, 'local.env')


class DevConfig(GlobalConfig):
    """Development Configuration"""

    class Config:
        env_file: str = os.path.join(envs_dir, 'dev.env')


class StagingConfig(GlobalConfig):
    """Staging Configuration"""

    class Config:
        env_file: str = os.path.join(envs_dir, 'staging.env')


class ProdConfig(GlobalConfig):
    """Production Configuration"""

    class Config:
        env_file: str = os.path.join(envs_dir, 'prod.env')


class TestConfig(GlobalConfig):
    """Test Configuration"""

    class Config:
        env_file: str = os.path.join(envs_dir, 'test.env')


class FactoryConfig:
    """Returns a config instance depending on the ENVIRONMENT variable."""

    def __init__(self, environment: Optional[str]) -> None:
        self.environment = environment

    def __call__(self) -> GlobalConfig:
        if self.environment == "local":
            return LocalConfig()

        elif self.environment == "dev":
            return DevConfig()

        elif self.environment == "staging":
            return StagingConfig()

        elif self.environment == "prod":
            return ProdConfig()

        elif self.environment == "test":
            return TestConfig()

        else:
            return GlobalConfig()
