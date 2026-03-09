# T3: Initialize Python AI Service with FastAPI

**Priority:** P0 | **Sprint:** S1 | **Dependencies:** T1

---

## SUMMARY

Create the Python backend service using FastAPI that will host YOLO plate detection and OCR inference endpoints.

## BACKGROUND / CONTEXT

The AI service is a critical component that processes video frames and performs license plate detection + OCR. FastAPI provides async performance for handling concurrent frame processing requests from the Tauri backend. This service will be spawned by Tauri and communicate via HTTP on localhost.

## SCOPE OF WORK

1. Create `/ai-service` directory structure:
   - `app/` - main application
   - `app/api/` - API routes
   - `app/services/` - business logic (future: YOLO, OCR)
   - `app/models/` - Pydantic models
   - `app/core/` - config, utilities
   - `tests/` - unit tests
   - `models/` - placeholder for ML model files
2. Create `requirements.txt` with:
   - `fastapi>=0.100.0`
   - `uvicorn[standard]>=0.23.0`
   - `python-multipart>=0.0.6`
   - `pydantic>=2.0.0`
   - `pydantic-settings>=2.0.0`
   - `opencv-python>=4.8.0`
   - `numpy>=1.24.0`
   - `ultralytics>=8.0.0` (YOLO)
   - `paddleocr>=2.7.0` or `easyocr>=1.7.0`
3. Create `app/main.py` with FastAPI app and health endpoint
4. Create `app/core/config.py` with Pydantic Settings
5. Create `app/api/routes.py` with placeholder `/detect` endpoint
6. Create `app/models/schemas.py` with request/response models:
   - `DetectRequest` (frame data)
   - `DetectResponse` (plate_text, bbox, confidence)
7. Add `.env.example` with configuration template
8. Create `run.py` entry point for uvicorn
9. Add `README.md` with setup and run instructions

## ACCEPTANCE CRITERIA

- [ ] `pip install -r requirements.txt` succeeds
- [ ] `python run.py` starts uvicorn server on port 8000
- [ ] `GET /health` returns `{"status": "ok"}`
- [ ] `POST /detect` endpoint exists (returns placeholder response)
- [ ] Pydantic models validate request/response correctly
- [ ] Configuration loads from environment variables
- [ ] README documents: setup, run, and test commands

## DEFINITION OF DONE

- FastAPI service runs successfully
- Health endpoint verified via curl/browser
- Code reviewed and merged
- README provides clear setup instructions
- Tests directory structure ready for future tests

## DEPENDENCIES

- T1 (Repository structure must exist)
- Python 3.10+ installed on dev machine

## TECHNICAL NOTES

Run on `localhost:8000` by default. Use async endpoints for better concurrency. Keep YOLO/OCR imports conditional to allow service to start without models during initial setup. Model files will be added separately.

## TESTING NOTES

- Run server: `python run.py`
- Test health: `curl http://localhost:8000/health`
- Test detect: `curl -X POST http://localhost:8000/detect -H "Content-Type: application/json" -d "{}"`
- Verify process can be killed and restarted cleanly

## SUGGESTED LABELS

`backend`, `python`, `fastapi`, `ai`, `setup`, `priority-critical`, `sprint-1`