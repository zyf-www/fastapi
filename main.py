from fastapi import FastAPI ,HTTPException
from routers import items, users, chat
from sqlmodel import SQLModel
import database as db
import models
app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)
app.include_router(chat.router)
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(db.engine)
@app.get("/")
def root():
    return {"原神nb"}

@app.get("/ping")
def ping():
    return {"原神不nb"}
# @app.get("/items/{item_id}")
# async def items(item_id: int):
#     return {"item_id": item_id}


