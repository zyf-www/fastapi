from rag.engine import ask
from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()
class ChatRequest(BaseModel):
    question: str
@router.post("/chat")
async def chat(question:ChatRequest):
    answer = ask(question.question)
    return {"answer": answer}