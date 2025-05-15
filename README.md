# News Classifier API

A 12-Factor–compliant FastAPI microservice that classifies news articles as **“REAL”** or **“FAKE”** using a scikit-learn pipeline. It loads a pre-trained `Pipeline` (TfidfVectorizer + LogisticRegression) from a pickle file, exposes a `/news/classify` endpoint, includes CORS, health checks, pytest coverage, and is fully containerized with Docker & Docker Compose.

---

## 🔗 Links

- **GitHub Repository**: https://github.com/Axkratos/News-Classifier
- **Demo Video**: https://www.youtube.com/watch?v=flTT5MHWjYA

## 🚀 Features

- **12-Factor App**:
  1. **Codebase**: single Git repo
  2. **Dependencies**: all in `requirements.txt`
  3. **Config**: via environment (`.env`) & Pydantic-Settings
  4. **Backing services**: model artifact treated as a “backing file”
  5. **Build/Release/Run**: Docker image + Compose
  6. **Processes**: stateless FastAPI process, no sticky state
  7. **Port binding**: configurable `$PORT`
  8. **Concurrency**: scale by running multiple containers
  9. **Disposability**: fast startup, graceful shutdown

10. **Dev/Prod parity**: same Docker Compose stack locally & in prod
11. **Logs**: JSON to stdout
12. **Admin processes**: one-off retraining (`src/cli/train_model.py`)

- **API Endpoints**

  - `GET  /health` → `{ "status": "ok" }`
  - `POST /news/classify` → `{ "label": "REAL"|"FAKE", "confidence": 0.0–1.0 }`

- **Testing**: Pytest suite (`tests/test_classify.py`) with FastAPI `TestClient`.

- **Containerization**:
  - **Dockerfile** (uses `requirements.txt`)
  - **docker-compose.yml** for easy local setup

---

## 🛠️ Prerequisites

- Python 3.8+
- Docker & Docker Compose (for containerized runs)
- (Optional) Virtual environment tool (venv, conda, etc.)

---

## ⚙️ Configuration

Copy `.env.example` to `.env` and adjust:

```dotenv
ALLOWED_HOSTS=["*"]
PORT=8000
MODEL_PATH=app/models/news_classifier_pipeline.pkl

```

---

## 🎲 Installation & Local Run

### 1. Clone & Create Virtual Environment

```bash
git clone https://github.com/Axkratos/News-Classifier.git
cd <working_directory>
python -m venv .env
# Windows PowerShell
env\Scripts\Activate
```

### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the Application

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Run Tests

```bash
pytest -q tests/test_classify.py
```

## Docker & Docker Compose

### 1. Build & Start

```bash
docker-compose build
docker-compose up
```

Health: GET http://localhost:8000/health

Classify: POST http://localhost:8000/news/classify

### 2. Tear Down

```bash
docker-compose down
```

## Contributing

1. Fork this repository
2. Create a feature branch (git checkout -b feature/your-feature)
3. Commit your changes with tests (git commit -m "Add new feature")
4. Push to your fork and open a Pull Request
