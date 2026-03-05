# Task Breakdown - License Plate Recognition Desktop App

> Aligned with PRD Phase 1 MVP scope: RTSP camera + plate detection/OCR + event storage + search

---

## Phase 1 - MVP

### 1.1 Project Setup

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| T1 | Repository structure | Create monorepo structure: `/src-tauri`, `/src`, `/ai-service` | P0 |
| T2 | Tauri + React + Vite init | Initialize Tauri v2 project with React + Vite frontend | P0 |
| T3 | Python AI service init | Create Python project with FastAPI for AI inference | P0 |
| T4 | Dev environment docs | Document required tools: Rust, Node, Python, OpenCV | P0 |

### 1.2 Camera Module

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| C1 | RTSP stream connection | Connect to IP camera via RTSP URL using OpenCV | P0 |
| C2 | Frame capture loop | Capture frames from RTSP stream at 5-10 FPS | P0 |
| C3 | Stream to frontend | Send video frames from Rust/Python to React UI | P0 |
| C4 | Camera CRUD API | Rust commands: add / edit / delete camera (name + RTSP URL) | P0 |
| C5 | Camera persistence | Store camera configs in SQLite | P0 |

### 1.3 AI Pipeline

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| A1 | Plate detection model | Integrate YOLO model to detect license plate region | P0 |
| A2 | OCR engine | Integrate PaddleOCR or EasyOCR for VN plate text extraction | P0 |
| A3 | 2-row plate handling | Pre-process 2-row motorcycle plates before OCR | P0 |
| A4 | Plate text cleanup | Normalize OCR output (remove noise, format VN plate pattern) | P0 |
| A5 | Detection API endpoint | FastAPI endpoint: receive frame -> return plate text + bbox + confidence | P0 |

### 1.4 Event Processing

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| E1 | Detection trigger | When AI returns plate text -> create detection event | P0 |
| E2 | Snapshot capture | Save cropped plate image + full frame to disk | P0 |
| E3 | Duplicate filtering | Suppress same plate detected within N seconds (configurable) | P0 |
| E4 | Event to frontend | Push new detection event to React UI in real-time | P0 |

### 1.5 Database

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| D1 | SQLite setup | Initialize SQLite database via Tauri/Rust | P0 |
| D2 | Schema design | Tables: `cameras` (id, name, rtsp_url, created_at), `events` (id, camera_id, plate_text, confidence, image_path, snapshot_path, detected_at) | P0 |
| D3 | Insert event | Store detection event with plate + image path + timestamp | P0 |
| D4 | Query events | Search by plate text (partial match), filter by time range | P0 |

### 1.6 Desktop UI

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| U1 | Camera dashboard | Main screen: live camera feed + latest detection overlay | P0 |
| U2 | Add camera dialog | Form to input camera name + RTSP URL | P0 |
| U3 | Detection panel | Sidebar showing latest detected plate + snapshot thumbnail | P0 |
| U4 | History table | Paginated table: plate, camera, time, thumbnail | P0 |
| U5 | Search bar | Search by plate number with partial match | P0 |
| U6 | Time filter | Date picker to filter history by date range | P0 |

### 1.7 Tauri Integration

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| TA1 | Rust commands | Bridge: camera CRUD, event queries, settings | P0 |
| TA2 | Python service comm | Rust spawns Python AI service, communicates via HTTP localhost | P0 |
| TA3 | Image file management | Save/read snapshots via Tauri fs API | P0 |

---

## Phase 2 - Enhancement

### 2.1 Multi Camera

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| MC1 | Multi stream handling | Run 2-4 RTSP streams concurrently | P1 |
| MC2 | Grid camera view | Display 2x2 camera grid in UI | P1 |
| MC3 | Camera filter in search | Filter events by camera source | P1 |

### 2.2 AI Improvements

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| AI1 | Confidence display | Show confidence score on detection panel | P1 |
| AI2 | Image enhancement | Pre-process frames for low light (CLAHE, histogram eq) | P1 |
| AI3 | ROI detection zone | Allow user to draw detection region on camera view | P1 |

### 2.3 Manual Override

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| MO1 | Edit plate text | Operator can correct OCR result in history | P1 |
| MO2 | Manual plate entry | Add plate record manually when detection fails | P1 |

### 2.4 System

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| SY1 | Error handling | Reconnect camera on disconnect, restart AI on crash | P1 |
| SY2 | Logging | Log system events and errors to file | P1 |
| SY3 | Settings panel | UI for app config (duplicate timeout, FPS, paths) | P1 |
| SY4 | System tray | Background running with tray icon | P1 |
| SY5 | Image preview | Full-size image viewer for snapshots | P1 |

---

## Phase 3 - Future

### 3.1 Parking Flow

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| PK1 | Camera role assignment | Mark camera as Entrance or Exit | P2 |
| PK2 | Session matching | Match entry plate with exit plate | P2 |
| PK3 | Duration calculation | Calculate parking time per session | P2 |
| PK4 | Active vehicle list | Show vehicles currently in lot | P2 |

### 3.2 Reporting & Data

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| RD1 | Daily summary | Stats: total vehicles by day | P2 |
| RD2 | Export CSV | Export detection records | P2 |
| RD3 | Auto backup | Scheduled SQLite backup | P2 |
| RD4 | Data retention | Auto-delete old records/images | P2 |

### 3.3 Performance & Packaging

| ID | Task | Description | Priority |
|----|------|-------------|----------|
| PP1 | GPU inference | CUDA acceleration for YOLO | P2 |
| PP2 | Build installer | Tauri build for Windows (primary) | P2 |
| PP3 | Bundle AI models | Package YOLO + OCR models with installer | P2 |
