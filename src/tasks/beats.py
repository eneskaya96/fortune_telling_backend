import logging

from datetime import datetime
from src.tasks.fortune.tasks import create_fortune
from src.worker import celery

logger = logging.getLogger(__name__)


@celery.task()
def beat_create_fortune() -> None:
    # TODO: create random fortune
    fortune = str(datetime.utcnow())
    logger.info(f'Fortune {fortune} queued')
    create_fortune.apply_async(kwargs={'fortune': fortune})
