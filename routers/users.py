from fastapi import FastAPI ,HTTPException ,APIRouter

from database import SessionDep
from sqlmodel import select
from models import User
router = APIRouter()


@router.get("/user")
async def user(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}



@router.post("/users/register")
async def register_user(user:User,session:SessionDep):
    existing_user = session.exec(select(User).where(User.username == user.username)).first()
    if existing_user:
        raise HTTPException(status_code = 400,detail="Username already registered")
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message":"User created successfully","user":user.username}

@router.get("/admin/dashboard")
async def admin_dashboard(token: str |None = None ):
    if token != "secret-token":
        raise HTTPException(status_code=401,detail="Token is invalid")
    return {"message":"Welcome Admin"}