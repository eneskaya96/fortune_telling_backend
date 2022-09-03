import abc
from typing import Optional

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.fortune.entities.fortune import Fortune


class FortuneRepository(BaseRepository[Fortune], abc.ABC):
    @abc.abstractmethod
    def get_fortune_with_offset(self, offset: int) -> Optional[Fortune]:
        pass
