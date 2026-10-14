
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Item(SQLModel, table=True):
    id: int |None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str |None = None

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True ,index=True)
    password: str