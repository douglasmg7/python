from typing import Annotated

from fastapi import Depends, HTTPException, Path, status

from app.dependencies.database import SessionDep
from app.models.user import User

UserId = Annotated[int, Path(ge=1, description="The user id to fetch")]


async def get_user_or_404(session: SessionDep, user_id: UserId) -> User:
    room = await session.get(User, user_id)
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return room


UserDep = Annotated[User, Depends(get_user_or_404)]
