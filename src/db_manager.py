import psycopg2


class DBManager:
    """Метод для работы с базами данных."""

    database_name: str
    params: dict

    def __init__(self, database_name: str, params: dict) -> None:
        """Абстрактный метод для инициализации данных класса работы с базами данных."""

        self.database_name = database_name
        self.params = params
        self.conn = psycopg2.connect(dbname=database_name, **params)
        self.cur = self.conn.cursor()

    def print_vacancies(self) -> None:
        """Метод для вывода вакансий."""

        vacancies: list = self.cur.fetchall()
        for vacancy in vacancies:
            formatted_vacancy: str = ", ".join(map(str, vacancy))
            print(formatted_vacancy)

        if not vacancies:  # если база данных пустая
            print("К сожалению, вакансий не было найдено.")

    def get_companies_and_vacancies_count(self) -> None:
        """Метод для получения всех компаний и количества вакансий у них."""
        query = """
            SELECT employer_name, COUNT(Vacancies.vacancy_url) as amount
            FROM Employers JOIN Vacancies USING(employer_id)
            GROUP BY employer_name ORDER BY employer_name
            """
        self.cur.execute(query)

    def get_all_vacancies(self) -> None:
        """Метод для получения всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки."""
        query = """
                SELECT Employers.employer_name, vacancy_name, salary, vacancy_url
                FROM Vacancies JOIN Employers USING(employer_id)
                ORDER BY Employers.employer_name
                """
        self.cur.execute(query)

    def get_avg_salary(self) -> None:
        """Метод для получения средней зарплаты по вакансиям."""
        query = """
                SELECT AVG(salary)
                FROM Vacancies
                """
        self.cur.execute(query)

    def get_vacancies_with_higher_salary(self) -> None:
        """Метод для получения списка всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        query = """
                SELECT Employers.employer_name, vacancy_name, salary, vacancy_url
                FROM Vacancies JOIN Employers USING(employer_id)
                WHERE salary > (SELECT AVG(salary) FROM Vacancies)
                ORDER BY salary DESC
                """
        self.cur.execute(query)

    def get_vacancies_with_keyword(self, keyword: str) -> None:
        """Метод для получения всех вакансий, в названии которых содержатся переданные в метод слова."""
        query = f"""
                SELECT Employers.employer_name, vacancy_name, salary, vacancy_url
                FROM Vacancies JOIN Employers USING(employer_id)
                WHERE vacancy_name LIKE '%{keyword}%'
                """
        self.cur.execute(query)
