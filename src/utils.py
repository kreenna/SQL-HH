import psycopg2


def create_database(database_name: str, params: dict) -> None:
    """Функция для автоматического создания базы данных."""

    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {database_name};")
    cur.execute(f"CREATE DATABASE {database_name};")

    conn.close()  # закрываем подключение

    conn = psycopg2.connect(dbname=database_name, **params)
    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute(
            """
                CREATE TABLE Employers (employer_id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    url TEXT,
                    vacancies_url TEXT,
                    trusted BOOLEAN
                );
            """
        )

    with conn.cursor() as cur:
        cur.execute(
            """
                CREATE TABLE Vacancies (
                    vacancy_id SERIAL PRIMARY KEY,
                    employer_id INT REFERENCES Employers(employer_id),
                    name VARCHAR NOT NULL,
                    salary VARCHAR NOT NULL,
                    vacancy_url TEXT,
                    requirements TEXT,
                    responsibilities TEXT
                );
            """
        )

    conn.close()  # закрываем подключение


def save_data_to_database(data: list, database_name: str, params: dict) -> None:
    """Сохранение данных о вакансиях и компаниях в базу данных."""

    conn = psycopg2.connect(dbname=database_name, **params)
    conn.autocommit = True

    with conn.cursor() as cur:
        for vacancy in data:
            employer_data: dict = vacancy["employer"]
            cur.execute(
                """
                INSERT INTO Employers (name, url, vacancies_url, trusted)
                VALUES (%s, %s, %s, %s)
                RETURNING employer_id;
                """,
                (
                    employer_data["name"],
                    employer_data["url"],
                    employer_data["vacancies_url"],
                    employer_data["trusted"],
                ),
            )
            vacancy_salary: dict = vacancy["salary"]

            # приводим зарплату к нужному формату
            salary_from: int = vacancy_salary["from"] if vacancy_salary["from"] else 0
            salary_to: int = vacancy_salary["to"] if vacancy_salary["to"] else 0
            currency: str = "RUB" if vacancy_salary["currency"] == "RUR" else vacancy_salary["currency"]
            salary: str = f"{salary_from}-{salary_to} {currency}"

            employer_id: int = cur.fetchone()[0]
            vacancy_data: dict = vacancy["snippet"]
            cur.execute(
                """
                    INSERT INTO Vacancies (employer_id, name, salary, vacancy_url, requirements, responsibilities)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                (
                    employer_id,
                    vacancy["name"],
                    salary,
                    vacancy["url"],
                    vacancy_data["requirement"],
                    vacancy_data["responsibility"],
                ),
            )

        conn.close()  # закрываем подключение
