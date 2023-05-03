from sqlalchemy.orm.session import Session
from typing import Type
from src.shared.repositories.default_repository import DefaultRepository
from src.modules.user.entities import 

class UserRepository(DefaultRepository):
    def __init__(self, session: Session, user: Type[UserEntity]):
        super().__init__(session, user)
