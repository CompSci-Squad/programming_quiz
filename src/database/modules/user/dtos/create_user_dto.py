from typing import TypedDict, Optional

class CreateUserDto(TypedDict):
    email: str
    password: str
    name: str
    ra: str
    coins: Optional[int]
    current_level_id: Optional[str]