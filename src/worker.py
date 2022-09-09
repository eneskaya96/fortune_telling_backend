from datetime import timedelta
from typing import Dict, Any

from celery import Celery

from src.configs.config_manager import WorkerConfigManager
from src.infrastructure.persistence.redis_manager import RedisManager

project_slug = 'fortune'

configuration = WorkerConfigManager.init_config()
RedisManager.init_redis(configuration)

config = {
    "broker_url": configuration.BROKER_URL,
    "task_ignore_result": True,
    "worker_concurrency": configuration.WORKER_CONCURRENCY,
    "worker_disable_rate_limits": True,
    "worker_hijack_root_logger": True
}
celery = Celery("tasks", broker=config.pop("broker_url"))
celery.conf.update(**config)

# task_queues must be defined in consumer
celery.conf.task_queues = {
    f'{project_slug}:beat_queue': {
        'queue_arguments': {'x-queue-mode': 'lazy'}
    },
    f'{project_slug}:create_fortune_queue': {
        'queue_arguments': {'x-queue-mode': 'lazy'}
    }
}

# task_routes of tasks that called from a worker must be defined in consumer
celery.conf.task_routes = [
    {'src.tasks.beats.*': {'queue': f'{project_slug}:beat_queue'}},
    {'src.tasks.fortune.tasks.*': {'queue': f'{project_slug}:create_fortune_queue'}}
]


def __prepare_beat_schedule() -> Dict[str, Any]:
    schedule: Dict[str, Any] = {
        'beat_create_fortune': {
            'task': 'src.tasks.beats.beat_create_fortune',
            'schedule': timedelta(seconds=configuration.BEAT_CREATE_FORTUNE_INTERVAL),
            'options': {'expires': configuration.EXPIRE_TIME_OF_TASKS}
        }
    }
    return schedule


celery.conf.beat_schedule = __prepare_beat_schedule()

import src.tasks  # NOQA
