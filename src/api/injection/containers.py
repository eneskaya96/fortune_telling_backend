from dependency_injector import containers, providers

from src.domain.fortune.services.fortune_service import FortuneService

from src.infrastructure.persistence.repositories.unit_of_work import UnitOfWork


class BaseContainer(containers.DeclarativeContainer):
    config = providers.Configuration()


class Repositories(BaseContainer):
    unit_of_work = providers.Factory(UnitOfWork)


class Services(BaseContainer):
    fortune_service = providers.Factory(FortuneService)
