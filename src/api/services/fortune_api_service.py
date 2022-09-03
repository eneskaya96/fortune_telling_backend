import logging
from typing import Optional

from src.api.models.dto.fortune.fortune_request_dto import FortuneRequestDto
from src.api.services.base.base_service import BaseService
from src.domain.fortune.entities.fortune import Fortune
from src.domain.seed_work.repository.unit_of_work import UnitOfWork
import random

from src.api.services.base.base_fortune_api_service import BaseFortuneApiService


class FortuneApiService(BaseFortuneApiService, BaseService):
    logger = logging.getLogger(__name__)

    def __init__(self, uow: Optional[UnitOfWork] = None) -> None:
        super().__init__(uow)

    def get_random_fortune(self) -> Fortune:
        """
        Returns a random fortune
        """
        random_offset = random.randint(0, 5)
        existing_fortune = self.uow.fortunes.get_fortune_with_offset(random_offset)
        if existing_fortune:
            return existing_fortune

        #random_words = RandomWords()
        #random_word = random_words.get_random_word()
        fortune = Fortune.create_fortune("random_word")

        return fortune

    def create_fortune(self, fortune_request_dto: FortuneRequestDto) -> Fortune:
        """
        Create a new fortune and returns it
        :param fortune_request_dto
        """

        new_fortune = Fortune.create_fortune(fortune_request_dto.fortune)

        with self.uow:
            self.uow.fortunes.insert(new_fortune)

        return new_fortune
