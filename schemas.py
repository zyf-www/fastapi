from pydantic import BaseModel


class item(BaseModel):
    name: str
    price: float
    description: str | None = None

class User(BaseModel):
    username: str
    password: str
