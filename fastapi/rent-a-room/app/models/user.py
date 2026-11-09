from typing import TYPE_CHECKING

from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.booking import Booking


# Shared field for all representation of room.
class UserBase(SQLModel):
    name: str
    email: EmailStr
    phone: PhoneNumber


# The payload to send back to the client.
class UserPublic(UserBase):
    id: int


# Map to database.
class User(UserBase, table=True):
    __tablename__: str = "users"

    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True)

    bookings: list["Booking"] = Relationship(back_populates="user")


class UserUpdate(SQLModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: PhoneNumber | None = None
