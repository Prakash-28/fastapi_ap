from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import User, UserCreate
from app.crud import create_user, get_user
from app.database import get_session

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_new_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    return await create_user(user, session)

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user(user_id, session)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
