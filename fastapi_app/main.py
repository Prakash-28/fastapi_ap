
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

# Database URL
DATABASE_URL = "postgresql+asyncpg://username:password@localhost/dbname"

# Create Async SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create Async Session
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Base model for SQLAlchemy
Base = declarative_base()

# Initialize FastAPI app
app = FastAPI()

# Dependency for creating a session
async def get_session():
    async with async_session() as session:
        yield session

@app.on_event("startup")
async def startup():
    # Initialize the database
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()

# Example Model
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

@app.post("/items/")
async def create_item(name: str, description: str = None, session: AsyncSession = Depends(get_session)):
    new_item = Item(name=name, description=description)
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item
