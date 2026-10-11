from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def root():
    return {"原神nb"}

@app.get("/ping")
def ping():
    return {"原神不nb"}
@app.get("/items/{item_id}")
async def items(item_id: int):
    return {"item_id": item_id}

@app.get("/user")
async def user(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


class items(BaseModel):
    name: str
    price: float
    description: str | None = None

@app.post("/items")
async def create_item(item: items):
    return item