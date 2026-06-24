from fastapi import FastAPI
from app.schemas import Room

app = FastAPI(
    title="StaySync API",
    description="Hotel Management System API",
    version="1.0.0"
)

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


@app.get("/")
def root():
    return {"message": "StaySync API is running!"}

@app.get("/rooms")
def get_rooms():
    return rooms

@app.get("/rooms/{room_id}")
def get_room(room_id: int):

    for room in rooms:
        if room.id == room_id:
            return room

    return {"error": "Room not found"}

@app.post("/rooms")
def create_room(room: Room):

    rooms.append(room)

    return {
        "message": "Room created successfully",
        "room": room
    }

