from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный метод для классов с API."""

    @abstractmethod
    def __init__(self) -> None:
        """Абстрактный метод для инициализации данных класса и API-сервиса."""
        pass

    @abstractmethod
    def get_api_response(self) -> list:
        """Абстрактный метод для получения ответа от API-сервиса."""
        pass
