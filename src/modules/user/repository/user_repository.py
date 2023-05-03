from sqlalchemy.orm.session import Session
from typing import Type
from src.shared.repositories.default_repository import DefaultRepository
from src.modules.user.entities.user_entity import UserEntity
from src.database.connect import session

class UserRepository(DefaultRepository[UserEntity]):
    def __init__(self, session: Session, user: Type[UserEntity]):
        super().__init__(session, user)

userRepo = UserRepository(session, UserEntity)

userRepo.create({})
