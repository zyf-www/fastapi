from fastapi import FastAPI ,HTTPException ,APIRouter
from schemas import User
router = APIRouter()


@router.get("/user")
async def user(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}



@router.post("/users/register")
async def register_user(user:User):
    if user.username == "admin":
        raise HTTPException(status_code = 400,detail="Username already registered")
    return user

@router.get("/admin/dashboard")
async def admin_dashboard(token: str |None = None ):
    if token != "secret-token":
        raise HTTPException(status_code=401,detail="Token is invalid")
    return {"message":"Welcome Admin"}