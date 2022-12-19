from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide, Closing


class Service:
    init_counter: int = 0
    shutdown_counter: int = 0

    @classmethod
    def reset_counter(cls):
        cls.init_counter = 0
        cls.shutdown_counter = 0

    @classmethod
    def init(cls):
        cls.init_counter += 1

    @classmethod
    def shutdown(cls):
        cls.shutdown_counter += 1


class FactoryService:
    def __init__(self, service: Service):
        self.service = service


def init_service():
    service = Service()
    service.init()
    yield service
    service.shutdown()


class Container(containers.DeclarativeContainer):

    service = providers.Resource(init_service)
    factory_service = providers.Factory(FactoryService, service)


@inject
def test_function(service: Service = Closing[Provide["service"]]):
    return service


@inject
def test_function_dependency(factory: FactoryService = Closing[Provide["factory_service"]]):
    return factory
