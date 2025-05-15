import joblib
from functools import lru_cache
from fastapi import HTTPException
from app.core.config import Settings

@lru_cache()
def get_model():
    try:
        model = joblib.load(Settings().MODEL_PATH)
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")
    return model


def predict(text: str) -> dict:
    model = get_model()
    prob = model.predict_proba([text])[0][1]
    label = "REAL" if prob >= 0.5 else "FAKE"
    return {"label": label, "confidence": float(prob)}