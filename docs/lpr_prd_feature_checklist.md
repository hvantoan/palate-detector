# PRD - Desktop License Plate Recognition App (Tauri)

## 1. Product Overview
Desktop app that connects to IP cameras via RTSP in LAN, detects vehicle license plates using AI, and stores recognition events locally. Target: Vietnamese license plates.

## 2. Target Users
- Parking operators
- Security guards

## 3. Product Goals
- Connect IP cameras via RTSP link in LAN
- Detect and OCR Vietnamese license plates in real time
- Store plate number + snapshot + timestamp locally
- Provide searchable detection history

## 4. Market & Locale
- Vietnam only
- Support Vietnamese plate formats (1-row car, 2-row motorcycle)
- Small scale: 1-4 cameras

---

# Feature Checklist

## Phase 1 - MVP (Current Focus)

| Category | Feature | Description | Priority | Status |
|----------|---------|-------------|----------|--------|
| Camera | Add camera | Add IP camera by entering RTSP URL | P0 | Pending |
| Camera | Camera preview | Display live RTSP stream in UI | P0 | Pending |
| Camera | Camera CRUD | Edit / remove camera sources | P0 | Pending |
| AI | Plate detection | Detect license plate region in frame (YOLO) | P0 | Pending |
| AI | OCR recognition | Extract text from plate (VN format) | P0 | Pending |
| AI | 2-row plate support | Handle 2-row motorcycle plates | P0 | Pending |
| Events | Detection trigger | Generate event when plate recognized | P0 | Pending |
| Events | Snapshot capture | Save image of detected plate + vehicle | P0 | Pending |
| Events | Duplicate filtering | Suppress repeated detection within N seconds | P0 | Pending |
| Storage | SQLite database | Store plate records locally | P0 | Pending |
| Storage | Image storage | Save snapshot images to local disk | P0 | Pending |
| UI | Camera dashboard | Main screen showing live camera feed | P0 | Pending |
| UI | Detection panel | Show latest detected plate + snapshot | P0 | Pending |
| UI | History table | List all detection events | P0 | Pending |
| Search | Plate search | Search by plate number (partial match) | P0 | Pending |
| Search | Time filter | Filter records by date/time range | P0 | Pending |

## Phase 2 - Enhancement

| Category | Feature | Description | Priority | Status |
|----------|---------|-------------|----------|--------|
| Camera | Multi camera view | Monitor 2-4 cameras simultaneously | P1 | Pending |
| AI | Confidence score | Display recognition confidence level | P1 | Pending |
| AI | Image enhancement | Pre-process frames for low light / night | P1 | Pending |
| Manual | Plate correction | Allow operator to edit OCR result | P1 | Pending |
| Manual | Manual plate entry | Enter plate manually when detection fails | P1 | Pending |
| Search | Camera filter | Filter events by camera source | P1 | Pending |
| UI | Image preview | View full-size captured image | P1 | Pending |
| UI | Settings panel | App and camera configuration UI | P1 | Pending |
| ROI | Detection zone | Draw region of interest on camera view | P1 | Pending |
| System | Error handling | Handle camera disconnect / AI failures | P1 | Pending |
| System | Logging | Record system events and errors | P1 | Pending |
| System | System tray | Run in background with tray icon | P1 | Pending |

## Phase 3 - Future

| Category | Feature | Description | Priority | Status |
|----------|---------|-------------|----------|--------|
| Parking | Entry/Exit flow | Camera role (in/out), session matching | P2 | Pending |
| Parking | Duration calc | Calculate parking duration | P2 | Pending |
| Parking | Active vehicles | List vehicles currently in lot | P2 | Pending |
| Report | Daily summary | Vehicle count by day | P2 | Pending |
| Report | Export CSV | Export detection data | P2 | Pending |
| Data | Auto backup | Scheduled SQLite backup | P2 | Pending |
| Data | Retention policy | Auto-delete old records / images | P2 | Pending |
| Perf | GPU inference | CUDA acceleration for AI model | P2 | Pending |
| System | AI configuration | Model selection and thresholds | P2 | Pending |

---

# Non Functional Requirements

| Category | Requirement |
|----------|-------------|
| Performance | Process at 5-10 FPS per camera |
| Accuracy | Plate OCR >90% (daytime), >85% (night) |
| Latency | Detection to display <500 ms |
| Reliability | Handle camera reconnect on disconnect |
| Storage | Support up to 100K records |
| Platform | Windows (primary), Linux/macOS via Tauri |

---

# Technical Stack

| Layer | Technology |
|-------|------------|
| Desktop Framework | Tauri |
| Frontend | React + Vite |
| Backend | Rust commands |
| AI Engine | Python service (YOLO + OCR) |
| Video Processing | OpenCV |
| Database | SQLite |

---

# Milestones

| Phase | Deliverables |
|-------|-------------|
| Phase 1 | Camera RTSP connection + live preview + plate detection + OCR + event storage + search UI |
| Phase 2 | Multi-camera + night enhancement + manual correction + ROI + system tray |
| Phase 3 | Parking flow + reporting + backup + performance optimization + packaging |

