from src.database.connect import connect_to_database
from src.modules.user.entities.user_entity import UserEntity
from src.modules.user.repository.user_repository import UserRepository


def main():
    session = connect_to_database()
    if session is not None:
        userRepo = UserRepository(session, UserEntity)
        userRepo.create()   



if __name__ == "__main__":
    main()
