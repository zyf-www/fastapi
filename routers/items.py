from fastapi import FastAPI ,HTTPException ,APIRouter
from schemas import Item
router = APIRouter()


@router.post("/items")
async def create_item(item: Item):
    return item

database ={
    1:"曼",
    2:"巴",
    3:"ou",
    4:"t"
}

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id  not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": database[item_id]}
