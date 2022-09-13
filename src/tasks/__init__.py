from typing import Any

from celery.signals import after_setup_logger
from src.worker import configuration
from src.infrastructure.logging.log_manager import LogManager


@after_setup_logger.connect
def celery_after_setup_logger(**kwargs: Any) -> None:
    LogManager.init_logger(configuration)

from src.tasks import beats  # NOQA
from src.tasks.fortune import tasks as fortune_tasks  # NOQA