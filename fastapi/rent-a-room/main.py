from contextlib import asynccontextmanager
from os import name
from typing import Annotated, Literal

from fastapi import Cookie, FastAPI, Header, HTTPException, Query, Response, status
from fastapi.staticfiles import StaticFiles

# from pydantic import AfterValidator
from pydantic import (
    BaseModel,
    Field,
    NonNegativeFloat,
    StringConstraints,
    field_validator,
)

from database import create_db_and_table

openapi_tags = [
    {
        "name": "rooms",
        "description": "Operation with **rooms** (a 4-wall _space_ that can be slept in)",
    }
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_table()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Renta a Room API",
    description="Book a stay in a house or room",
    version="1.0.23",
    contact={"name": "DMG", "email": "a@a.com"},
    openapi_tags=openapi_tags,
)

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

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


class AppCookies(BaseModel):
    theme: Literal["dark", "light"] = "dark"
    language: Literal["en", "es"] = "en"


class AppHeader(BaseModel):
    user_agent: str | None = None


class RoomsQueryParams(BaseModel):
    max_price: int | None = Field(
        default=None, ge=10, le=10_000, examples=[100, 200, 10_000]
    )
    search: Annotated[str | None, StringConstraints(to_lower=True)] = Field(
        default=None,
        min_length=3,
        max_length=10,
        title="Search term",
        description="Provide a keyword to look for within the room's title",
        examples=["sunny", "bedroom", "house"],
    )

    @field_validator("search")
    @classmethod
    def fail_if_funny(cls, search: str) -> str:
        if "lol" in search:
            raise ValueError("No funny business allowed")
        return search


@app.get("/", status_code=status.HTTP_200_OK)
def root(
    app_cookies: Annotated[AppCookies, Cookie()],
    app_headers: Annotated[AppHeader, Header()],
):
    greetings = {"en": "Welcome", "es": "Bienvenido"}
    greeting = greetings.get(app_cookies.language)

    return {"message": greeting, "User-Agent": app_headers.user_agent}


# http://localhost:8000/rooms?search=bedroom&max_price=200
@app.get(
    "/rooms",
    status_code=status.HTTP_200_OK,
    tags=["rooms"],
    summary="List all available rooms",
    description="Return all rooms. Supports filtering by price and search term.",
    response_description="A list of rooms matching the filter criteria.",
)
def get_rooms(params: Annotated[RoomsQueryParams, Query()]):
    results = [apartment, house, studio]

    if params.max_price:
        results = [
            room for room in results if room["price_per_night"] <= params.max_price
        ]

    if params.search:
        results = [room for room in results if params.search in room["name"].lower()]

    return results


@app.get(
    "/rooms/mansions",
    status_code=status.HTTP_200_OK,
    tags=["rooms", "mansions"],
    deprecated=True,
)
def get_mansions(params: Annotated[RoomsQueryParams, Query()]):
    results = [house]

    if params.max_price:
        results = [
            room for room in results if room["price_per_night"] <= params.max_price
        ]

    if params.search:
        results = [room for room in results if params.search in room["name"].lower()]

    return results


@app.get("/rooms/{room_id}", status_code=status.HTTP_200_OK, tags=["rooms"])
def get_room(room_id: int):
    for room in [apartment, house, studio]:
        if room["id"] == room_id:
            return room
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")


@app.get("/preferences", status_code=status.HTTP_200_OK, tags=["preferences"])
def set_preferences(response: Response):
    app_cookies = AppCookies()
    response.set_cookie(key="theme", value=app_cookies.theme)
    response.set_cookie(key="language", value=app_cookies.language)
    return {"message": "preferences updated"}
