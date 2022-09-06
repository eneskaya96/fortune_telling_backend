import logging

from src.tasks.fortune.fortune_worker_service import FortuneWorkerService
from src.worker import celery

logger = logging.getLogger(__name__)


@celery.task()
def create_fortune(fortune: str) -> None:
    FortuneWorkerService.create_fortune(fortune)
