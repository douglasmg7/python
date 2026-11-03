from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles

from app.dependencies.database import create_db_and_table
from app.routers import booking, general, room

openapi_tags = [
    {
        "name": "rooms",
        "description": "Operation with **rooms** (a 4-wall _space_ that can be slept in)",
    }
]


def log_request(request: Request):
    print(f"{request.method} - {request.url}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_table()
    yield


app = FastAPI(
    lifespan=lifespan,
    # dependencies=[Depends(log_request)],
    title="Renta a Room API",
    description="Book a stay in a house or room",
    version="1.0.23",
    contact={"name": "DMG", "email": "a@a.com"},
    openapi_tags=openapi_tags,
)
app.include_router(general.router)
app.include_router(room.router, prefix="/rooms", tags=["room"])
app.include_router(booking.router, prefix="/booking", tags=["booking"])

app.mount("/assets", StaticFiles(directory="assets"), name="assets")
