from contextlib import asynccontextmanager
from os import name, stat
from typing import Annotated, Literal

from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    status,
)
from fastapi.staticfiles import StaticFiles

# from pydantic import AfterValidator
from pydantic import (
    BaseModel,
    Field,
    NonNegativeFloat,
    StringConstraints,
    field_validator,
)
from sqlmodel import col, desc, func, select

from database import SessionDep, create_db_and_table
from models import Room, RoomBase, RoomPublic, RoomUpdate

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
    limit: int = Field(default=10, ge=1, le=100)
    offset: int = Field(default=0, ge=0)

    @field_validator("search")
    @classmethod
    def fail_if_funny(cls, search: str) -> str:
        if "lol" in search:
            raise ValueError("No funny business allowed")
        return search


RoomId = Annotated[int, Path(ge=1, description="The id room to fetch")]


def get_room_or_404(session: SessionDep, room_id: RoomId) -> Room:
    room = session.get(Room, room_id)
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Room not found"
        )
    return room


RoomDep = Annotated[Room, Depends(get_room_or_404)]


@app.get("/", status_code=status.HTTP_200_OK)
def root(
    app_cookies: Annotated[AppCookies, Cookie()],
    app_headers: Annotated[AppHeader, Header()],
    session: SessionDep,
):
    greetings = {"en": "Welcome", "es": "Bienvenido"}
    greeting = greetings.get(app_cookies.language)

    return {"message": greeting, "User-Agent": app_headers.user_agent}


@app.post(
    "/rooms",
    status_code=status.HTTP_201_CREATED,
    tags=["rooms"],
    response_model=RoomPublic,
)
def create_room(session: SessionDep, room: RoomBase):
    room = Room.model_validate(room)
    session.add(room)
    session.commit()
    session.refresh(room)
    return room


# http://localhost:8000/rooms?search=bedroom&max_price=200
@app.get(
    "/rooms",
    status_code=status.HTTP_200_OK,
    tags=["rooms"],
    response_model=list[RoomPublic],
    summary="List all available rooms",
    description="Return all rooms. Supports filtering by price and search term.",
    response_description="A list of rooms matching the filter criteria.",
)
def get_rooms(session: SessionDep, params: Annotated[RoomsQueryParams, Query()]):
    statement = select(Room)

    if params.max_price:
        statement = statement.where(Room.price_per_night <= params.max_price)

    if params.search:
        statement = statement.where(func.lower(Room.name).contains(params.search))
        # statement = statement.where(col(Room.name).ilike(f"%{params.search}%"))

    statement = (
        statement.order_by(col(Room.id)).offset(params.offset).limit(params.limit)
    )

    return session.exec(statement).all()


@app.get(
    "/rooms/{room_id}",
    status_code=status.HTTP_200_OK,
    tags=["rooms"],
    response_model=RoomPublic,
)
def get_room(room: RoomDep):
    return room


@app.patch(
    "/rooms/{room_id}",
    status_code=status.HTTP_200_OK,
    tags=["rooms"],
    response_model=RoomPublic,
)
def update_room(session: SessionDep, room: RoomDep, room_payload: RoomUpdate):
    room.sqlmodel_update(room_payload.model_dump(exclude_unset=True))
    session.add(room)
    session.commit()
    session.refresh(room)
    return room


@app.delete(
    "/rooms/{room_id}",
    status_code=status.HTTP_200_OK,
    tags=["rooms"],
    response_model=RoomPublic,
)
def delete_room(session: SessionDep, room: RoomDep):
    session.delete(room)
    session.commit()
    return room


@app.get("/preferences", status_code=status.HTTP_200_OK, tags=["preferences"])
def set_preferences(response: Response):
    app_cookies = AppCookies()
    response.set_cookie(key="theme", value=app_cookies.theme)
    response.set_cookie(key="language", value=app_cookies.language)
    return {"message": "preferences updated"}
