# app/api/routes/classify.py

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
    # 1. Concatenate title + text
    raw = f"{item.title or ''} {item.text or ''}".strip()
    if not raw:
        raise HTTPException(status_code=400, detail="Empty content")

    # 2. Delegate to predict(...)
    try:
        result = predict(raw)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return Prediction(**result)
