from pydantic import BaseModel

class Room(BaseModel):
    id: int
    room_number: int
    type: str
    available: bool
