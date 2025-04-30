import json

import requests

from src.abstract_classes import Parser


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
        self._employer_id = []
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {
            "text": "",
            "page": 0,
            "per_page": 100,
            "employer_id": [],
            "only_with_salary": True,
        }
        self.vacancies = []

    def get_api_response(self, employer_ids: list, keyword: str = "") -> str:
        """Метод для получения ответа от API-сервиса."""

        self.__params["employer_id"] = employer_ids  # устанавливаем слово для поиска вакансий

        if keyword:
            self.__params["text"] = keyword  # устанавливаем слово для поиска вакансий

        while self.__params.get("page") != 20:  # проверяем, что количество страниц не выше 20
            response = requests.get(self.url, headers=self.__headers, params=self.__params)

            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.__params["page"] += 1

        return json.dumps(self.vacancies, ensure_ascii=False, indent=4)
