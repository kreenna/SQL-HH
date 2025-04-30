from abc import ABC


class Parser(ABC):
    """Абстрактный метод для классов с API."""

    def init(self) -> None:
        """Абстрактный метод для инициализации данных класса и API-сервиса."""
        pass

    def get_api_response(self, employer_ids: list, keyword: str = "") -> str:
        """Абстрактный метод для получения ответа от API-сервиса."""
        pass


class DataBase(ABC):
    """Абстрактный метод для классов с базами данных."""

    def init(self) -> None:
        """Абстрактный метод для инициализации данных класса работы с базами данных."""
        pass

    def get_companies_and_vacancies_count(self):
        """Метод для получения всех компаний и количества вакансий у них."""
        pass

    def get_all_vacancies(self):
        """Метод для получения всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки."""
        pass

    def get_avg_salary(self):
        """Метод для получения средней зарплаты по вакансиям."""
        pass

    def get_vacancies_with_higher_salary(self):
        """Метод для получения списка всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    def get_vacancies_with_keyword(self):
        """Метод для получения всех вакансий, в названии которых содержатся переданные в метод слова."""
        pass
