from fastapi import FastAPI
from app.database import database, metadata, engine
from app.api import endpoints

metadata.create_all(bind=engine)
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(endpoints.router)
