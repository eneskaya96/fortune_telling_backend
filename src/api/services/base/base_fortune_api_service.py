import abc

from src.domain.fortune.entities.fortune import Fortune


class BaseFortuneApiService(abc.ABC):
    @abc.abstractmethod
    def get_random_fortune(self) -> Fortune:
        pass
