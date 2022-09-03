from typing import Optional

from src.domain.fortune.entities.fortune import Fortune as DomainFortune
from src.domain.fortune.repositories.fortune_repository import FortuneRepository as FortuneDomainRepository
from src.infrastructure.entities.fortune_management.fortune import Fortune
from src.infrastructure.persistence.repositories.base_repository import BaseGenericRepository


class FortuneRepository(BaseGenericRepository[DomainFortune], FortuneDomainRepository):

    def __init__(self) -> None:
        super().__init__(Fortune, DomainFortune)

    def get_fortune_with_offset(self, offset: int) -> Optional[Fortune]:
        return self.query.one_or_none()
