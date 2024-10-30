from sqlalchemy.future import select
from app.models import users
from app.database import get_session
from app.schemas import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def create_user(user: UserCreate, session: AsyncSession):
    new_user = users.insert().values(name=user.name, email=user.email)
    await session.execute(new_user)
    await session.commit()
    return {**user.dict(), "id": new_user.inserted_primary_key[0]}

async def get_user(user_id: int, session: AsyncSession):
    query = select(users).where(users.c.id == user_id)
    result = await session.execute(query)
    return result.fetchone()
