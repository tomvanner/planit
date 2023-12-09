from pydantic import Field

from planit.schemas import PlanitBase


class UserSchema(PlanitBase):
    name: str = Field(min_length=1, max_length=128)
