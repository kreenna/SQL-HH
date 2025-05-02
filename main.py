from config import config

from src.hh_api import HeadHunterAPI
from src.utils import create_database, save_data_to_database

def main():
    """Основная функция для взаимодействия с пользователем."""

    parameters: dict = config()
    # автоматически создаем базу данных
    create_database("headhunter", parameters)

    hh_api: HeadHunterAPI = HeadHunterAPI() # создаем экземпляр класса
    vacancies_data: list = hh_api.get_api_response()
    # автоматически добавляем вакансии и компании в базу данных
    save_data_to_database(vacancies_data, "headhunter", parameters)

    while True:  # запускаем цикл работы с вакансиями
        user_option = input(
            """Какую информацию вы желаете получить?
1 - список всех компаний и количества вакансий от них;
2 - список всех вакансий и данных о них;
3 - средняя зарплата по всем вакансиям;
4 - список вакансий, у которых зарплата выше средней;
5 - вакансии по ключевому слову.
(Введите цифру от 1 до 5)\n"""
        )

        if user_option == "1":  # проверяем каждый вариант
            pass

        elif user_option == "2":  # проверяем каждый вариант
            pass

        elif user_option == "3":  # проверяем каждый вариант
            pass

        elif user_option == "4":  # проверяем каждый вариант
            pass

        elif user_option == "5":  # проверяем каждый вариант
            keyword: str = input("Введите ключевое слова для поиска:\n")


        else:   # если ввод пользователя некорректный
            print("К сожалению, такого варианта не существует.")
            continue

        finish_option: str = input("Желаете завершить работу с вакансиями? (да/нет)\n")

        if finish_option == "да":   # завершаем работу, если ответ положительный
            break

if __name__ == "__main__":
    main()
