from dataclasses import dataclass

@dataclass
class UserDto:
    username: str
    password: str
    email: str
    first_name: str
    last_name: str