from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

from src.shared.logger.logger import LOGGER


def connect_to_database():
    load_dotenv()
    # config do banco de dados
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")

    if SQLALCHEMY_DATABASE_URI is not None:
        # Create database engine
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        LOGGER.info("connected to db")

        # Create database session
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
