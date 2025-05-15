# app/services/predict.py

import joblib
import numpy as np
from functools import lru_cache
from app.core.config import Settings

@lru_cache()
def get_model():
    """
    Load the single Pipeline .pkl that contains:
      - your TextCleaner
      - TfidfVectorizer
      - LogisticRegression
    """
    path = Settings().MODEL_PATH
    try:
        model = joblib.load(path)
    except Exception as e:
        raise RuntimeError(f"Failed to load model from {path}: {e}")
    return model

def predict(text: str) -> dict:
    """
    text: a single raw string (already cleaned by TextCleaner in-pipeline)
    returns: {"label": "REAL"/"FAKE", "confidence": float}
    """
    model = get_model()

    # get 2-column probs; find which column is “REAL” (label=1)
    probs  = model.predict_proba([text])[0]
    classes = model.classes_
    # assume you trained with 0=FAKE, 1=REAL
    try:
        real_idx = int(np.where(classes == 1)[0][0])
    except IndexError:
        # fallback if labels reversed or different
        real_idx = 1 if len(classes) > 1 else 0

    real_prob = float(probs[real_idx])
    label = "REAL" if real_prob >= 0.5 else "FAKE"

    return {"label": label, "confidence": real_prob}
