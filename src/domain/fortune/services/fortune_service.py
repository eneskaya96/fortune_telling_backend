import logging
from src.domain.fortune.entities.fortune import Fortune


class FortuneService:
    logger = logging.getLogger(__name__)

    @staticmethod
    def create_fortune(fortune: str) -> Fortune:
        return Fortune.create_fortune(fortune)
