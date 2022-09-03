from typing import Optional

from src.api.services.base.base_api_services import BaseApiServices
from src.api.services.fortune_api_service import FortuneApiService
from src.domain.seed_work.repository.unit_of_work import UnitOfWork


class ApiServices(BaseApiServices):
    def __init__(self, uow: Optional[UnitOfWork] = None) -> None:
        self._uow: Optional[UnitOfWork] = uow
        self.fortune_api_service: Optional[FortuneApiService] = None

    @property
    def fortune(self) -> FortuneApiService:
        if not self.fortune_api_service:
            self.fortune_api_service = FortuneApiService(self._uow)
        return self.fortune_api_service
