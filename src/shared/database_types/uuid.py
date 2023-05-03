import uuid
from sqlalchemy import TypeDecorator, CHAR

class UUID(TypeDecorator):
    impl = CHAR(32)

    def process_bind_param(self, value):
        if value is not None:
            return str(value)
        return None

    def process_result_value(self, value):
        if value is not None:
            return uuid.UUID(value)
        return None
