from __future__ import annotations
from typing import List, TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer
from src.shared.entities.base_entity import Base

if TYPE_CHECKING:
    from src.database.modules.user.entities.user_entity import UserEntity

class LevelEntity(Base):
    __tablename__ = "level"

    __id: Mapped[int] = mapped_column(
        Integer, name="id", autoincrement=True, primary_key=True
    )
    __question: Mapped[str] = mapped_column(String(80), name="question", nullable=False)
    __right_answer: Mapped[str] = mapped_column(
        String(80), name="right_answer", nullable=False
    )
    __reward: Mapped[int] = mapped_column(Integer, name="reward", nullable=False)
    __wrong_answer_1: Mapped[str] = mapped_column(
        String(80), name="wrong_answer_1", nullable=False
    )
    __wrong_answer_2: Mapped[str] = mapped_column(String(80), name="wrong_answer_2", nullable=False)
    __wrong_answer_3: Mapped[str] = mapped_column(String(80), name="wrong_answer_3", nullable=False)

    users: Mapped[List[UserEntity]] = relationship(back_populates="level")

    def __init__(
        self,
        question: str,
        right_answer: str,
        reward: int,
        wrong_answer_1: str,
        wrong_answer_2: str,
        wrong_answer_3: str,
    ):
        self.__question = question
        self.__right_answer = right_answer
        self.__reward = reward
        self.__wrong_answer_1 = wrong_answer_1
        self.__wrong_answer_2 = wrong_answer_2
        self.__wrong_answer_3 = wrong_answer_3

    @property
    def id(self):
        return self.__id

    @property
    def right_answer(self):
        return self.__right_answer

    @right_answer.setter
    def right_answer(self, value: str):
        self.__right_answer = value

    @property
    def reward(self):
        return self.__reward

    @reward.setter
    def reward(self, value: int):
        self.__reward = value

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, value: str):
        self.__question = value

    @property
    def wrong_answer_1(self):
        return self.__wrong_answer_1

    @wrong_answer_1.setter
    def wrong_answer_1(self, value: str):
        self.__wrong_answer_1 = value

    @property
    def wrong_answer_2(self):
        return self.__wrong_answer_2

    @wrong_answer_2.setter
    def wrong_answer_2(self, value: str):
        self.__wrong_answer_2 = value

    @property
    def wrong_answer_3(self):
        return self.__wrong_answer_3

    @wrong_answer_3.setter
    def wrong_answer_3(self, value: str):
        self.__wrong_answer_3 = value
