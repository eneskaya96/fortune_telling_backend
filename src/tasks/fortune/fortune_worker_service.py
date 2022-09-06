
from src.infrastructure.clients.fortune_api_client import FortuneApiClient


class FortuneWorkerService:

    @staticmethod
    def create_fortune(fortune: str) -> None:
        return FortuneApiClient.create_fortune(fortune)
