from fastapi import FastAPI

app = FastAPI(
    title="StaySync API",
    description="Hotel Management System API",
    version="1.0.0"
)

rooms = [
    {
        "id": 1,
        "room_number": 101,
        "type": "King",
        "available": True
    },
    {
        "id": 2,
        "room_number": 102,
        "type": "Double Queen",
        "available": False
    }
]



@app.get("/")
def root():
    return {"message": "StaySync API is running!"}

@app.get("/rooms")
def get_rooms():
    return rooms
    