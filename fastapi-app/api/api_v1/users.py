from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models.user import User

import core.config
from core.schemas.user import UserRead, UserCreate

router = APIRouter(
    prefix=core.config.settings.api.v1.users,
    tags=["Users"],
)

@router.get("" , response_model=list[UserRead])
async def get_users(session: AsyncSession = Depends(db_helper.session_getter))->Sequence[User]:
    stmt =select(User).order_by(User.id)
    users = await session.scalars(stmt)
    return users.all()


@router.post("/singup", response_model=UserRead)
async def create_user(user_create: UserCreate, session: AsyncSession = Depends(db_helper.session_getter)) -> User:
    user = User(**user_create.dict())  # Используем dict() для получения данных
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

