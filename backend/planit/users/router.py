from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from planit.database import get_db
from .schemas import UserSchema
from .models import User


router = APIRouter()


@router.get(
    "/",
    response_model=list[UserSchema],
    summary="Gets all users in the system",
)
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await User.get_all(db)
    return users
