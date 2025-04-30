import json

import requests

from src.abstract_api import Parser


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter."""

    url: str
    _employer_id: list
    headers: dict
    params: dict
    vacancies: list

    def __init__(self) -> None:
        """Метод для инициализации данных класса и API-сервиса."""

        self.url = "https://api.hh.ru/vacancies"
        self._employer_id = [
            "7944",
            "10545773",
            "78989",
            "14208",
            "3986000",
            "10337252",
            "2848751",
            "4786273",
            "9426910",
            "87021",
        ]
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {
            "page": 0,
            "per_page": 100,
            "employer_id": [],
            "only_with_salary": True,
        }
        self.vacancies = []

    def get_api_response(self) -> str:
        """Метод для получения ответа от API-сервиса."""

        self.__params["employer_id"] = (
            self._employer_id
        )  # устанавливаем слово для поиска вакансий

        while (
            self.__params.get("page") != 20
        ):  # проверяем, что количество страниц не выше 20
            response = requests.get(
                self.url, headers=self.__headers, params=self.__params
            )

            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.__params["page"] += 1

        return json.dumps(self.vacancies, ensure_ascii=False, indent=4)
