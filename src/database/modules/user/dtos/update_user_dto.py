from typing import TypedDict, Optional

class UpdateUserDto(TypedDict):
    id: str
    email: Optional[str]
    password: Optional[str]
    name: Optional[str]
    ra: Optional[str]
    coins: Optional[int]
    current_level_id: Optional[str]