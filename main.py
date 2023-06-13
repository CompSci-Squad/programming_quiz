import uuid
from src.database import connect_to_database
from src.database.modules.level.repositories.level_repository import LevelRepository
from src.database.modules.user.repository.user_repository import UserRepository


def main():
    print("teste")
    session = connect_to_database()
    if session:

        test_level = LevelRepository(session)
        # test_user = UserRepository(session)
        test_level.create(
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

    """ test_user.create(
        {
            "email": "nathy.neto.bataglia@gmail.com",
            "password": "batataFrita123",
            "current_level_id": level.id,
            "name": "nathalia",
            "ra": "23.00375-8",
            "coins": 0,
        }
    ) """

    # print(test_user.get_all())
    # print(test_user.get_by_id('990bcaa37513489784c0db6ac3508498'))
    # print(test_user.find_user('ra', '23.00375-8'))
    # test_user.update({"id": user_found.id, 'email': 'test@example.com'})


if __name__ == "__main__":
    main()
