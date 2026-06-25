from fastapi import APIRouter
from app.schemas import Room

router = APIRouter()

rooms = [
    Room(
        id=1,
        room_number=101,
        type="King",
        available=True
    ),
    Room(
        id=2,
        room_number=102,
        type="Double Queen",
        available=False
    )
]

@router.get("/rooms")
def get_rooms();
    return rooms


@router.get("/rooms/{room_id}")
def get_room(room_id: int):

    for room in rooms:
        if room.id == room_id:
            return room

    return {"error":"Room not found"} 

@router.post("/rooms")
def create_room(room: Room)

    rooms.append(room)

    return {
        "message": "Room created succesfully",
        "room": room
    }

    