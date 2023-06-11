import uuid
from src.database import connect_to_database
from src.database.modules.level.repositories.level_repository import LevelRepository
from src.database.modules.user.repository.user_repository import UserRepository


def main():
    print("teste")
    session = connect_to_database()
    test_level = LevelRepository(session)
    test_user = UserRepository(session)
    level = test_level.create(
        {
            "question": "o que e classificacao vocal?",
            "right_answer": "tipo de voz do cantor",
            "reward": 20,
            "wrong_answer": (
                "a nota que ele alcança",
                "se ele canta bem",
                "ranking de voz do cantor",
            ),
        }
    )

    test_user.create(
        {
            "email": "nathy.neto.bataglia@gmail.com",
            "password": "batataFrita123",
            "current_level_id": level.id,
            "name": "nathalia",
            "ra": "23.00375--8",
            "coins": 0,
        }
    )


if __name__ == "__main__":
    main()
