from typing import Annotated, Literal

from fastapi import APIRouter, Cookie, Header, Response, status
from pydantic import BaseModel

router = APIRouter()


class AppCookies(BaseModel):
    theme: Literal["dark", "light"] = "dark"
    language: Literal["en", "es"] = "en"


class AppHeader(BaseModel):
    user_agent: str | None = None


@router.get("/", status_code=status.HTTP_200_OK)
def root(
    app_cookies: Annotated[AppCookies, Cookie()],
    app_headers: Annotated[AppHeader, Header()],
):
    greetings = {"en": "Welcome", "es": "Bienvenido"}
    greeting = greetings.get(app_cookies.language)

    return {"message": greeting, "User-Agent": app_headers.user_agent}


@router.get("/preferences", status_code=status.HTTP_200_OK)
def set_preferences(response: Response):
    app_cookies = AppCookies()
    response.set_cookie(key="theme", value=app_cookies.theme)
    response.set_cookie(key="language", value=app_cookies.language)
    return {"message": "preferences updated"}
