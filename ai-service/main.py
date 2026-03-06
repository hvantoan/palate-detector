"""
Palate Detector - License Plate Recognition AI Service

FastAPI service for license plate detection and OCR.
Uses YOLO for plate detection and PaddleOCR/EasyOCR for text recognition.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import get_settings
from routers import router as detection_router

settings = get_settings()

app = FastAPI(
    title="Palate Detector AI Service",
    description="License Plate Recognition API",
    version="0.1.0",
)

# Configure CORS middleware for Tauri frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(detection_router)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {"status": "ok", "service": "palate-detector-ai"}


@app.get("/health")
async def health():
    """Health check endpoint for monitoring."""
    return {"status": "ok"}