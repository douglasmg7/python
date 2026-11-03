from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel
from sqlmodel.main import relationship

if TYPE_CHECKING:
    from app.models.booking import Booking


# Shared field for all representation of room.
class RoomBase(SQLModel):
    name: str = Field()
    price_per_night: int = Field()
    bedrooms: float = Field(multiple_of=0.5)
    bathrooms: float = Field(multiple_of=0.5)


# The payload to send back to the client.
class RoomPublic(RoomBase):
    id: int


# Map to database.
class Room(RoomBase, table=True):
    __tablename__: str = "rooms"

    id: int | None = Field(default=None, primary_key=True)

    bookings: list["Booking"] = Relationship(back_populates="room")


class RoomUpdate(SQLModel):
    name: str | None = None
    price_per_night: int | None = None
    bedrooms: float | None = None
    bathrooms: float | None = None
