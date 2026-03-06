# T3: Initialize Python AI Service with FastAPI

## SUMMARY

Create Python project with FastAPI serving as the AI inference service for license plate detection and OCR processing.

## BACKGROUND / CONTEXT

- LPR app uses a separate Python service for AI inference (YOLO detection + OCR)
- Tauri/Rust backend communicates with this service via HTTP localhost
- FastAPI chosen for async support, auto-generated docs, and high performance
- This service will host endpoints for frame processing, plate detection, and text extraction

## SCOPE OF WORK

1. Create `/ai-service` directory with Python project structure:
   - `ai-service/main.py` - FastAPI app entry point
   - `ai-service/requirements.txt` - Python dependencies
   - `ai-service/routers/` - API route modules
   - `ai-service/services/` - Business logic (detection, OCR)
   - `ai-service/models/` - Pydantic request/response schemas
   - `ai-service/config.py` - Configuration (model paths, thresholds)
2. Set up virtual environment (`venv`) with install script
3. Add core dependencies: `fastapi`, `uvicorn`, `python-multipart`, `opencv-python-headless`, `numpy`
4. Create health check endpoint: `GET /health` -> `{"status": "ok"}`
5. Create placeholder detection endpoint: `POST /detect` -> accepts image, returns mock response
6. Configure CORS middleware (allow Tauri localhost origin)
7. Add `run.py` or CLI command to start uvicorn server on configurable port (default 8100)
8. Verify server starts and responds to health check

## ACCEPTANCE CRITERIA

- [ ] `python main.py` or `python run.py` starts FastAPI server on `http://localhost:8100`
- [ ] `GET /health` returns `{"status": "ok"}` with 200
- [ ] `POST /detect` accepts multipart image upload, returns mock JSON response with plate_text, bbox, confidence fields
- [ ] Swagger docs accessible at `/docs`
- [ ] Virtual environment setup script works on Windows
- [ ] All dependencies install without errors via `pip install -r requirements.txt`
- [ ] Project follows clean structure with separation of concerns (routers, services, models)

## DEFINITION OF DONE

- [ ] Python project scaffolded in `/ai-service`
- [ ] Server starts and endpoints respond correctly
- [ ] `requirements.txt` locked with versions
- [ ] Setup instructions documented
- [ ] Code reviewed and merged

## DEPENDENCIES

- **T1** (Repository structure) - folder layout must exist
- Python 3.10+ installed on dev machine
- No dependency on T2 (can be done in parallel)

## TECHNICAL NOTES

- Use `uvicorn` with `--reload` for development
- Keep FastAPI app minimal - no auth, no DB connection (AI service is stateless)
- Detection endpoint schema (for future use):
  ```json
  {
    "plates": [
      {
        "plate_text": "51F-123.45",
        "confidence": 0.95,
        "bbox": [x1, y1, x2, y2]
      }
    ]
  }
  ```
- Port 8100 to avoid conflicts with common dev ports (3000, 5173, 8000, 8080)
- `opencv-python-headless` (not `opencv-python`) to avoid GUI dependency issues

## TESTING NOTES

- Manual: start server, hit `/health` with curl or browser
- Manual: POST image to `/detect`, verify mock response structure
- Manual: verify `/docs` Swagger UI loads
- Future: unit tests for detection/OCR services (not in this task scope)

## SUGGESTED LABELS

`setup`, `backend`, `ai`, `python`, `P0`, `phase-1`
