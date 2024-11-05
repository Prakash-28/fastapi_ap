from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas
from ..database import get_db

# Create a router instance for item routes
router = APIRouter()

# Endpoint to create a new item
@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

# Endpoint to get all items
@router.get("/", response_model=List[schemas.Item])
def get_all_items(db: Session = Depends(get_db)):
    return crud.get_items(db=db)
