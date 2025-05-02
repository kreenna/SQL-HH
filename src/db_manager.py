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

    def get_companies_and_vacancies_count(self) -> None:
        """Метод для получения всех компаний и количества вакансий у них."""
        query = """
            SELECT company_title, COUNT(vacancy_name) as vacancies
            FROM companies JOIN vacancies USING(company_id)
            GROUP BY company_title
            """
        self.cur.execute(query)

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
