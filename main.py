from src.database.connect import connect_to_database
from src.modules.user.entities.user_entity import UserEntity
from src.modules.user.repository.user_repository import UserRepository


def main():
    session = connect_to_database()
    if session is not None:
        userRepo = UserRepository(session)
        user = UserEntity(username="teste", password="testando", email="teste@teste.com")
        userRepo.create(user)



if __name__ == "__main__":
    main()
