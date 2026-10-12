from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def root():
    return {"原神nb"}

@app.get("/ping")
def ping():
    return {"原神不nb"}
# @app.get("/items/{item_id}")
# async def items(item_id: int):
#     return {"item_id": item_id}

@app.get("/user")
async def user(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


class item(BaseModel):
    name: str
    price: float
    description: str | None = None

class User(BaseModel):
    username: str
    password: str

@app.post("/items")
async def create_item(item: item):
    return item

database ={
    1:"曼",
    2:"巴",
    3:"ou",
    4:"t"
}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id  not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": database[item_id]}

@app.post("/users/register")
async def register_user(user:User):
    if user.username == "admin":
        raise HTTPException(status_code = 400,detail="Username already registered")
    return user

@app.get("/admin/dashboard")
async def admin_dashboard(token: str |None = None ):
    if token != "secret-token":
        raise HTTPException(status_code=401,detail="Token is invalid")
    return {"message":"Welcome Admin"}
