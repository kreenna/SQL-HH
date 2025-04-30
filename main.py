from config import config
from src.utils import create_database, get_youtube_data, save_data_to_database


def main():
    """Основная функция для взаимодействия с пользователем."""
    employer_ids = [
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
    params = config()

    data = get_youtube_data(employer_ids)
    create_database("Employers", params)
    save_data_to_database(data, "Employers", params)


if __name__ == "__main__":
    main()
