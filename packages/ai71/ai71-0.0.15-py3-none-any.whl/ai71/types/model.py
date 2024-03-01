import enum
from typing import Optional


class Model(str, enum.Enum):
    FALCON_180B = "tiiuae/falcon-180b-chat"

    FALCON_40B = "tiiuae/falcon-40b"

    FALCON_40B_INSTRUCT = "tiiuae/falcon-40b-instruct"

    FALCON_7B = "tiiuae/falcon-7b"

    FALCON_7B_INSTRUCT = "tiiuae/falcon-7b-instruct"

    @classmethod
    def _missing_(cls, value: object) -> Optional["Model"]:
        if not isinstance(value, str):
            return None
        value = value.lower()
        for member in cls:
            if member.lower() == value:
                return member
        return None