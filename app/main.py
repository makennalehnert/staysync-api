from fastapi import FastAPI

from app.routers import rooms


app = FastAPI(
    title="StaySync API",
    description="Hotel Management System API",
    version="1.0.0"
)

app.include_router(rooms.router)


@app.get("/")
def root():
    return {"message": "StaySync API is running!"}


