from src.database import connect_to_database
from src.database.modules.level.repositories.level_repository import LevelRepository
from src.database.modules.user.repository.user_repository import UserRepository
# from src.modules.screens.game.game_screen import jogo
from src.modules.screens.user_screen.user_screen import user_screen


def main():
    session = connect_to_database()
    if session:

        """ test_level = LevelRepository(session)
        jogo(test_level) """

        test_user = UserRepository(session)
        user_screen(test_user)

       


if __name__ == "__main__":
    main()
