from sqlalchemy.orm.session import Session
from typing import List, Optional, Union
from src.database.modules.phase.entities.phase_entity import PhaseEntity
from src.shared.logger.logger import LOGGER


class PhaseRepository:
    __session: Session

    def __init__(self, session: Session):
        self.__session = session

    def create(self, name: str) -> Union[PhaseEntity, None]:
        try:
            entity = PhaseEntity(name)
            self.__session.add(entity)
            self.__session.commit()
            self.__session.refresh(entity)
            return entity
        except:
            LOGGER.error("error on creating a user")

    def update(self, id: str, name: Optional[str]) -> Union[PhaseEntity, None]:
        try:
            phase = self.get_by_id(id)
            if phase is None:
                LOGGER.error(f"no user found with {id}")
                raise ValueError()
            if name:
                phase.name = name

            self.__session.commit()
            self.__session.refresh(phase)
            return phase
        except:
            LOGGER.error("erro no update")

    def delete(self, id: str):
        phase = self.get_by_id(id)
        self.__session.delete(phase)
        self.__session.commit()

    def get_all(self) -> List[PhaseEntity]:
        return self.__session.query(PhaseEntity).all()

    def get_by_id(self, id: str) -> Union[PhaseEntity, None]:
        return self.__session.query(PhaseEntity).get(id)

    def find(
        self, name: Optional[str] = None, id: Optional[str] = None
    ) -> List[PhaseEntity] | None:
        try:
            query = self.__session.query(PhaseEntity)
            if name:
                query = query.filter(PhaseEntity.name == name)
            if id:
                query.filter(PhaseEntity.id == id)
            results = query.all()
            return results
        except:
            LOGGER.error("deu merda")
