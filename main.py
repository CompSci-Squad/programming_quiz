import uuid
from src.database import connect_to_database
from src.database.modules.user import UserRepository

def main():
    print("teste")
    session = connect_to_database()
    teste = UserRepository(session)

    teste.create()


if __name__ == "__main__":
    main()
