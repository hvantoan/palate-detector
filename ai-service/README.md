# Palate Detector AI Service

A Python FastAPI service for license plate detection and OCR processing. This service serves as the AI inference layer for the Palate Detector LPR (License Plate Recognition) application.

## Overview

This service provides a REST API for processing images and returning license plate detection results with:
- Plate text recognition
- Confidence scores
- Bounding box coordinates

Currently uses mock responses for development. Future versions will integrate YOLO for plate detection and PaddleOCR/EasyOCR for text recognition.

## Requirements

- **Python**: 3.10 or higher
- **Operating System**: Windows, macOS, or Linux

## Quick Start

### Option 1: Using the Setup Script (Windows)

```powershell
# Run the automated setup script
.\setup_venv.ps1

# Activate the virtual environment
.\.venv\Scripts\Activate.ps1

# Start the server
python run.py
```

### Option 2: Manual Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Windows (CMD):
.\.venv\Scripts\activate.bat
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python run.py
```

## Running the Server

### Development Mode (with auto-reload)

```bash
# Using the run script
python run.py

# Or directly with uvicorn
uvicorn main:app --host 0.0.0.0 --port 8100 --reload
```

### Production Mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8100
```

### Custom Port

```bash
# Using environment variable
PORT=9000 python run.py

# Or with uvicorn directly
uvicorn main:app --host 0.0.0.0 --port 9000
```

## API Endpoints

Once the server is running, the following endpoints are available:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root endpoint with service info |
| `/health` | GET | Health check for monitoring |
| `/detect/` | POST | License plate detection |
| `/docs` | GET | Swagger UI documentation |
| `/redoc` | GET | ReDoc documentation |
| `/openapi.json` | GET | OpenAPI specification |

### Health Check

```bash
curl http://localhost:8100/health
# Response: {"status": "ok"}
```

### Detection Endpoint

```bash
# Upload an image for plate detection
curl -X POST http://localhost:8100/detect/ \
  -F "file=@path/to/image.jpg"
```

**Response:**

```json
{
  "plates": [
    {
      "plate_text": "51F-123.45",
      "confidence": 0.95,
      "bbox": [100, 100, 300, 150]
    }
  ]
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `plates` | array | List of detected license plates |
| `plates[].plate_text` | string | Recognized text from the plate |
| `plates[].confidence` | float | Detection confidence (0.0-1.0) |
| `plates[].bbox` | array[int] | Bounding box [x1, y1, x2, y2] |

**Supported Image Formats:**
- JPEG
- PNG
- WebP

**Maximum File Size:** 10MB

### Error Responses

| Status Code | Description |
|-------------|-------------|
| 400 | Bad request (empty file, invalid image, file too large) |
| 500 | Internal server error |

## Configuration

The service can be configured via environment variables or a `.env` file:

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` | Server host address |
| `PORT` | `8100` | Server port |
| `RELOAD` | `false` | Enable auto-reload for development |
| `LOG_LEVEL` | `INFO` | Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) |
| `CONFIDENCE_THRESHOLD` | `0.5` | Minimum confidence for plate detection |
| `NMS_THRESHOLD` | `0.4` | Non-maximum suppression threshold |
| `MAX_UPLOAD_SIZE` | `10485760` | Max upload size in bytes (10MB) |

### Example `.env` file

```env
PORT=8100
HOST=0.0.0.0
RELOAD=true
LOG_LEVEL=DEBUG
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | >=0.110.0 | Web framework |
| `uvicorn[standard]` | >=0.27.0 | ASGI server |
| `python-multipart` | >=0.0.9 | File upload support |
| `opencv-python-headless` | >=4.9.0 | Image processing (no GUI) |
| `numpy` | >=1.26.0 | Numerical computing |
| `pydantic-settings` | >=2.0.0 | Configuration management |

> **Note:** `opencv-python-headless` is used instead of `opencv-python` to avoid GUI dependencies on headless servers.

## Project Structure

```
ai-service/
├── main.py              # FastAPI application entry point
├── run.py               # Uvicorn server startup script
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project metadata
├── setup_venv.ps1       # Windows setup script
├── models/
│   ├── __init__.py
│   └── schemas.py       # Pydantic request/response models
├── routers/
│   ├── __init__.py
│   └── detection.py     # Detection API routes
└── services/
    ├── __init__.py
    └── detection.py     # Detection business logic
```

## API Documentation

Interactive API documentation is available when the server is running:

- **Swagger UI**: http://localhost:8100/docs
- **ReDoc**: http://localhost:8100/redoc
- **OpenAPI JSON**: http://localhost:8100/openapi.json

## Development

### Running Tests

```bash
# Install test dependencies (when available)
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

### Code Style

This project follows Python best practices:
- Type hints for all function parameters and returns
- Docstrings for all public functions and classes
- Pydantic models for data validation
- Async handlers for all route endpoints

## Troubleshooting

### Port Already in Use

If port 8100 is already in use:

```bash
# Use a different port
PORT=8200 python run.py
```

### Virtual Environment Issues

```powershell
# Remove and recreate the virtual environment
Remove-Item -Recurse -Force .venv
.\setup_venv.ps1
```

### Import Errors

Make sure you've activated the virtual environment before running:

```bash
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Verify activation
Get-Command python
# Should show: .venv\Scripts\python.exe
```

## License

Copyright 2026 - Palate Detector AI Service

## Contributing

This service is part of the Palate Detector LPR application. See the main project repository for contribution guidelines.