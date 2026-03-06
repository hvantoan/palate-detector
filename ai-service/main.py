"""
Palate Detector - License Plate Recognition AI Service

FastAPI service for license plate detection and OCR.
Uses YOLO for plate detection and PaddleOCR/EasyOCR for text recognition.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Palate Detector AI Service",
    description="License Plate Recognition API",
    version="0.1.0",
)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {"status": "ok", "service": "palate-detector-ai"}


@app.get("/health")
async def health():
    """Health check endpoint for monitoring."""
    return {"status": "healthy"}