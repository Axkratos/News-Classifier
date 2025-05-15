from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.classify import router as classify_router
from app.core.config import Settings

settings = Settings()
app = FastAPI(title="News Classifier API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(classify_router, prefix="/news", tags=["classification"])

@app.get("/health")
def health_check():
    return {"status": "ok"}