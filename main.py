import pygame

from src.database import connect_to_database
from src.database.modules.level.repositories.level_repository import LevelRepository
from src.database.modules.user.repository.user_repository import UserRepository
from src.modules.screens.game.game_screen import jogo
from src.modules.screens.user_screen.user_screen import user_screen
from src.shared.enums.game_state_enum import GameState


def main():
    pygame.init()
    gameState = GameState.USER
    run = True
    session = connect_to_database()
    if session:
        userRepository = UserRepository(session)
        levelRepository = LevelRepository(session)
        while run:
            user = None

            if gameState == GameState.USER:
                user = user_screen(userRepository)
                if user:
                    gameState = GameState.GAME

            if gameState == GameState.GAME:
                jogo(levelRepository, user, userRepository)

            pygame.display.flip()


if __name__ == "__main__":
    main()
