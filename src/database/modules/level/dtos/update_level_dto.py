from typing import Optional, TypedDict, Tuple

class UpdateLevelDto(TypedDict):
    id: int
    question: Optional[str]
    right_answer: Optional[str]
    reward: Optional[int]
    wrong_answer: Optional[Tuple[str, str, str]]