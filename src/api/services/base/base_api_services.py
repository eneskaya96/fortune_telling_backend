import abc

from src.api.services.base.base_fortune_api_service import BaseFortuneApiService


class BaseApiServices(abc.ABC):
    @property
    @abc.abstractmethod
    def fortune(self) -> BaseFortuneApiService:
        pass
