from typing import TypedDict, Tuple

class CreateLevelDto(TypedDict):
    question: str
    right_answer: str
    reward: int
    wrong_answer: Tuple[str, str, str]