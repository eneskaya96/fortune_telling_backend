from typing import Optional
from redis import Redis
from src.configs.base_config import BaseConfig
from src.domain.seed_work.error.configuration_error import ConfigurationError


class RedisManager:
    __redis_instance: Optional[Redis] = None

    @classmethod
    def init_redis(cls, config: BaseConfig) -> None:
        if config.REDIS_HOST and config.REDIS_PORT:
            # No check for REDIS_CROPPED_PASSWORD and REDIS_CROPPED_DB in local and test env
            if config.ENVIRONMENT in ('test', 'local') or config.REDIS_PASSWORD:
                cls.__redis_instance = Redis(
                    host=config.REDIS_HOST,
                    port=config.REDIS_PORT,
                    password=config.REDIS_PASSWORD,
                    db=config.REDIS_DB,
                    decode_responses=True)

    @classmethod
    def get_redis(cls) -> Redis:
        if not cls.__redis_instance:
            raise ConfigurationError('Redis DB is not initialized.', 'redis_not_initialized')
        return cls.__redis_instance
