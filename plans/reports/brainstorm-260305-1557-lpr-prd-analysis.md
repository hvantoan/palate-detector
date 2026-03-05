# PRD Analysis Report - LPR Desktop App

**Date:** 2026-03-05
**Context:** Vietnam only | Bai giu xe | 1-4 camera | Software only
**Type:** Brainstorm / GAP Analysis

---

## 1. Executive Summary

PRD hien tai cover tot phan foundation (camera, AI, storage, search) nhung **thieu nghiem trong core business logic cho bai giu xe**. Cac GAP lon nhat: Entry/Exit flow, VN plate specifics, manual override, night handling.

---

## 2. Diem Manh Hien Tai

- Tech stack hop ly: Tauri + React + Rust + Python AI
- Priority phan chia ro rang P0-P2
- NFR co de cap latency, accuracy, FPS targets
- Task breakdown chi tiet, co dependency logic
- Multi-camera support da co trong ke hoach

---

## 3. GAP Analysis

### GAP 1: Entry/Exit Flow (CRITICAL - Core Business Logic)

Bai giu xe VN hoat dong theo mo hinh: Xe vao -> chup bien -> ghi thoi gian -> Xe ra -> khop voi luot vao -> tinh thoi gian -> tinh phi -> cho ra.

PRD chi "detect plate + luu event" ma **khong co logic ghep cap vao/ra**.

**Features can bo sung:**

| Feature | Description | Priority |
|---------|------------|----------|
| Camera role assignment | Gan camera la "Entrance" hoac "Exit" | P0 |
| Parking session | Ghep bien so xe vao <-> xe ra thanh 1 session | P0 |
| Duration calculation | Tinh thoi gian do xe | P0 |
| Pricing engine | Tinh phi theo thoi gian / loai xe | P1 |
| Active vehicles list | Danh sach xe dang trong bai | P0 |
| Occupancy counter | Dem slot con trong | P1 |
| Manual checkout | Operator xu ly xe khong match duoc | P1 |

### GAP 2: Vietnamese Plate Format (CRITICAL)

| Issue | Detail |
|-------|--------|
| 2-row plates | Xe may VN pho bien bien 2 hang -> OCR can xu ly khac |
| Plate size variance | Bien xe may nho hon nhieu bien o to |
| VN font training | Font chu bien VN khac bien quoc te |
| Special plates | Bien tam, ngoai giao, quan doi, cong an |
| Province codes | 2 ky tu dau = tinh/thanh -> can database mapping |

### GAP 3: Manual Override / Correction (HIGH)

| Feature | Description | Priority |
|---------|------------|----------|
| Plate text edit | Operator sua ket qua OCR sai | P0 |
| Manual plate entry | Nhap tay khi camera khong detect duoc | P0 |
| Low-confidence queue | Danh sach detection can review | P1 |
| Image comparison | So sanh anh xe vao vs xe ra | P1 |

### GAP 4: Night / Low Light Handling (HIGH)

| Feature | Description | Priority |
|---------|------------|----------|
| Image enhancement | Pre-processing anh truoc khi OCR | P1 |
| IR camera support | Ho tro camera hong ngoai | P1 |
| Adaptive thresholds | Tu dong dieu chinh threshold theo dieu kien sang | P2 |

### GAP 5: ROI - Region of Interest (MEDIUM)

| Feature | Description | Priority |
|---------|------------|----------|
| ROI drawing | Ve vung detect tren camera preview | P1 |
| Detection zone | Chi detect trong vung da chon | P1 |

### GAP 6: Reporting & Statistics (MEDIUM)

| Feature | Description | Priority |
|---------|------------|----------|
| Daily summary | Thong ke xe vao/ra theo ngay | P1 |
| Revenue report | Bao cao doanh thu (neu co pricing) | P2 |
| Export CSV | Xuat du lieu cho ke toan | P1 |
| Peak hours chart | Bieu do gio cao diem | P2 |

### GAP 7: Data Safety (MEDIUM)

| Feature | Description | Priority |
|---------|------------|----------|
| Auto backup SQLite | Tu dong backup database dinh ky | P1 |
| Export/Import DB | Xuat va nhap lai toan bo data | P2 |
| Image cleanup policy | Xoa anh cu tu dong de tiet kiem disk | P2 |

---

## 4. Features Nen Ha Priority (YAGNI)

| Feature hien tai | Priority hien tai | De xuat | Ly do |
|-----------------|-------------------|---------|-------|
| API endpoint | P2 | Remove/P3 | Quy mo nho, chi phan mem |
| Barrier control | P2 | Remove | User chon "chi phan mem" |
| AI configuration | P2 | P2 (giu) | Preset la du cho 1-4 camera |
| Local access control | P2 | P3 | Desktop app, 1 may |

---

## 5. NFR Dieu Chinh

| NFR hien tai | De xuat | Ly do |
|-------------|---------|-------|
| 15-30 FPS processing | 5-10 FPS | Bai xe khong can 30FPS, tiet kiem resource |
| >95% accuracy | >90% (day) / >85% (night) | Bien VN 2 hang + ban dem realistic hon |
| 1M records | 100K records | 1-4 cam, bai nho, du cho nhieu nam |
| Detection delay <200ms | <500ms | Bai xe khong can phan ung sieu nhanh |

---

## 6. Updated Feature Checklist (De xuat)

### P0 - Must Have (MVP)

| Category | Feature |
|----------|---------|
| Camera | Camera connection (USB/RTSP/IP) |
| Camera | Camera preview (live stream) |
| Camera | Camera role assignment (Entrance/Exit) |
| Camera | Camera configuration (add/edit/remove) |
| AI | Vehicle detection (YOLO) |
| AI | Plate detection (region) |
| AI | OCR recognition (VN plate format) |
| AI | 2-row plate support |
| Events | Event detection trigger |
| Events | Snapshot capture |
| Parking | Parking session (entry/exit matching) |
| Parking | Active vehicles list |
| Parking | Duration calculation |
| Manual | Plate text correction |
| Manual | Manual plate entry |
| Storage | SQLite database |
| Storage | Image storage |
| Search | Plate search |
| Search | Time filter |
| UI | Camera dashboard |
| UI | Detection panel |
| UI | History table |
| UI | Active parking list |
| System | App configuration |

### P1 - Should Have

| Category | Feature |
|----------|---------|
| Camera | Multi camera support (up to 4) |
| AI | Confidence score |
| AI | Image enhancement (night) |
| Events | Duplicate filtering |
| Parking | Pricing engine |
| Parking | Occupancy counter |
| Manual | Low-confidence review queue |
| Manual | Image comparison (in vs out) |
| Search | Camera filter |
| ROI | Detection zone drawing |
| Report | Daily summary |
| Report | Export CSV |
| UI | Image preview viewer |
| UI | Settings panel |
| Data | Auto backup SQLite |
| System | Error handling & logging |
| System | System tray (background) |

### P2 - Nice to Have

| Category | Feature |
|----------|---------|
| AI | Adaptive thresholds |
| AI | Vehicle type classification |
| Parking | Revenue report |
| Report | Peak hours chart |
| Data | Export/Import DB |
| Data | Image cleanup policy |
| Data | Data retention policy |
| System | Crash recovery |
| System | AI model config |
| Perf | GPU inference (CUDA) |

---

## 7. Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|-----------|
| OCR accuracy VN plates | Core function failure | Fine-tune model tren dataset VN, fallback manual entry |
| Night detection quality | Miss 30%+ events | Image enhancement pipeline, IR camera recommendation |
| Session mismatch | Sai tinh phi | Manual override + image comparison UI |
| SQLite corruption | Mat toan bo data | Auto backup + WAL mode |
| Python AI service crash | System down | Health check + auto restart |

---

## 8. Unresolved Questions

1. Dataset bien so VN nao se dung de train/fine-tune OCR model?
2. Co can phan biet xe may vs o to de tinh phi khac nhau khong?
3. Co can ho tro in ve/receipt (du la qua printer thuong) khong?
4. Pricing model cu the: theo gio, theo luot, theo ngay?
5. Co can luu video clip (ngoai snapshot) khi detect khong?
