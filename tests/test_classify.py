import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.predict import get_model

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

@pytest.mark.parametrize("title,text", [
    ("Hello","This is a test."),
])
def test_classify_endpoint(title, text):
    
    model = get_model()
    assert model is not None

    payload = {"title": title, "text": text}
    resp = client.post("/news/classify", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "label" in data and "confidence" in data
    assert isinstance(data["confidence"], float)