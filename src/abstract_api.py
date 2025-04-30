from abc import ABC


class Parser(ABC):
    """Абстрактный метод для классов с API."""

    def init(self) -> None:
        """Абстрактный метод для инициализации данных класса и API-сервиса."""
        pass

    def get_api_response(self) -> str:
        """Абстрактный метод для получения ответа от API-сервиса."""
        pass
