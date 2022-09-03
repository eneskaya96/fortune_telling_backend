import os
from pathlib import Path
from pydantic import Field, Extra
from typing import Optional
from src.configs.base_config import BaseConfig

envs_dir = os.path.join(Path(__file__).parent.parent.parent.absolute(), 'envs')


class GlobalConfig(BaseConfig):
    """Global Configuration"""

    """Secrets"""

    """Configurations"""

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
