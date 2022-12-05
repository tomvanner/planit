from pydantic import BaseModel


class Room(BaseModel):
    name: str
    cards: list[str]