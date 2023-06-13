from sqlalchemy.orm.session import Session
from typing import Union, List
from src.shared.logger.logger import LOGGER

from src.database.modules.level.entities.level_entity import LevelEntity
from src.database.modules.level.dtos.create_level_dto import CreateLevelDto
from src.database.modules.level.dtos.update_level_dto import UpdateLevelDto


class LevelRepository:
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, levelPayload: CreateLevelDto) -> LevelEntity:
        try:
            entity = LevelEntity(
                question=levelPayload["question"],
                right_answer=levelPayload["right_answer"],
                reward=levelPayload["reward"],
                wrong_answer_1=levelPayload["wrong_answer"][0],
                wrong_answer_2=levelPayload["wrong_answer"][1],
                wrong_answer_3=levelPayload["wrong_answer"][2],
            )

            self.__session.add(entity)
            self.__session.commit()
            self.__session.refresh(entity)
            LOGGER.info(f"Level created {entity}")
            return entity
        except Exception:
            LOGGER.error("error on creating level")
            raise Exception

    def update(self, updateLevelDto: UpdateLevelDto) -> Union[LevelEntity, None]:
        try:
            (id, question, right_answer, reward, wrong_answer) = updateLevelDto.values()
            level = self.get_by_id(id)

            if level is None:
                LOGGER.error("Could not find level")
                raise ValueError()

            if question is not None:
                level.question = question
            if right_answer is not None:
                level.right_answer = right_answer
            if reward is not None:
                level.reward = reward
            if wrong_answer is not None:
                level.wrong_answer_1 = wrong_answer[0]
                level.wrong_answer_2 = wrong_answer[1]
                level.wrong_answer_3 = wrong_answer[2]

            self.__session.commit()
            self.__session.refresh(level)
            LOGGER.info(f"updated level {level}")
            return level
        except Exception:
            LOGGER.error("error on updating level")
            raise Exception

    def delete(self, id: str):
        try:
            entity = self.get_by_id(id)
            if not entity:
                raise ValueError("entity not found")

            self.__session.delete(entity)
            self.__session.commit()
            LOGGER.info(f"Level deleted {entity}")
        except Exception:
            LOGGER.error("error on deleting level")
            raise Exception

    def get_by_id(self, id: str) -> Union[LevelEntity, None]:
        return self.__session.query(LevelEntity).get(id)
    
    def get_all(self) -> List[LevelEntity]:
        return self.__session.query(LevelEntity).all()
