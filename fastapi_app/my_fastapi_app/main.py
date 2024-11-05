from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import items

# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include the item routes using APIRouter
app.include_router(items.router, prefix="/items", tags=["items"])
