from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.predict import predict

router = APIRouter()

class NewsItem(BaseModel):
    title: str
    text: str

class Prediction(BaseModel):
    label: str
    confidence: float

@router.post("/classify", response_model=Prediction)
def classify(item: NewsItem):
    raw = f"{item.title} {item.text}".strip()
    if not raw:
        raise HTTPException(status_code=400, detail="Empty content")
    return predict(raw)