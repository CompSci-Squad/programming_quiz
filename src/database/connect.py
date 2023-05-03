from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

# config do banco de dados
SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_DATABASE_PEM = getenv('SQLALCHEMY_DATABASE_PEM')

if SQLALCHEMY_DATABASE_URI is not None:
    # Create database engine
    engine = create_engine(
        SQLALCHEMY_DATABASE_URI, connect_args={"ssl": {"key": SQLALCHEMY_DATABASE_PEM}}
    )

    # Create database session
    Session = sessionmaker(bind=engine)
    session = Session()
