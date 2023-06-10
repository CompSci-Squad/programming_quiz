import uuid
from src.database import connect_to_database
from src.database.modules.user import UserRepository

def main():
    print("teste")
    session = connect_to_database()
    teste = UserRepository(session)

    teste.create({'email': 'teste@example.com', 'password': 'test', 'name': 'douglas', 'ra': '23.00375-8', 'coins': 5})


if __name__ == "__main__":
    main()
