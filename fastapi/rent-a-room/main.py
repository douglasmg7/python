from os import name
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query, status
from fastapi.staticfiles import StaticFiles

apartment = {
    "id": 1,
    "name": "Sunny 2-bedroom apartment",
    "price_per_night": 200,
    "bedrooms": 2,
    "bathrooms": 1.5,
}
house = {
    "id": 2,
    "name": "Cozy 3-bedroom house",
    "price_per_night": 350,
    "bedrooms": 3,
    "bathrooms": 2.5,
}
studio = {
    "id": 3,
    "name": "Modern studio near museum",
    "price_per_night": 150,
    "bedrooms": 1,
    "bathrooms": 1,
}

app = FastAPI(
    title="Renta a Room API",
    description="Book a stay in a house or room",
    version="1.0.23",
    contact={"name": "DMG", "email": "a@a.com"},
)

app.mount("/assets", StaticFiles(directory="assets"), name="assets")


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Welcome to Rent a Room"}


# http://localhost:8000/rooms?search=bedroom&max_price=200
# max_price is a optional parameter.
@app.get("/rooms", status_code=status.HTTP_200_OK)
def get_rooms(
    max_price: int | None = None,
    search: Annotated[str | None, Query(min_length=3, max_length=10)] = "",
):
    results = [apartment, house, studio]

    if max_price:
        results = [room for room in results if room["price_per_night"] <= max_price]

    if search:
        results = [
            room for room in results if search.casefold() in room["name"].casefold()
        ]

    return results


@app.get("/rooms/{room_id}", status_code=status.HTTP_200_OK)
def get_room(room_id: int):
    for room in [apartment, house, studio]:
        if room["id"] == room_id:
            return room
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
