from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from pydantic import BaseModel, Field, StringConstraints, field_validator
from sqlmodel import col, func, select

from app.dependencies.database import SessionDep
from app.models.booking import Booking, BookingBase, BookingPublic
from app.models.room import Room

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BookingPublic)
async def create_booking(session: SessionDep, booking: BookingBase):
    room = await session.get(Room, booking.room_id)
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Room no exist"
        )
    validated_booking = Booking.model_validate(booking)
    session.add(validated_booking)
    await session.commit()
    await session.refresh(validated_booking)
    return validated_booking


@router.get(
    "/{booking_id}", status_code=status.HTTP_200_OK, response_model=BookingPublic
)
async def get_booking(session: SessionDep, booking_id: Annotated[int, Path(ge=1)]):
    booking = await session.get(Booking, booking_id)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Booking no exist"
        )
    return booking
