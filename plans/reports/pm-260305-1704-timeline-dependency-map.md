# PM Report: Timeline & Dependency Map - LPR Desktop App

**Date:** 2026-03-05 | **Phase:** Phase 1 MVP | **Status:** Planning
**Total Tasks:** 27 (Phase 1) | **Estimated Sprints:** 6 (1 sprint = 1 week)

---

## 1. Dependency Map (BlockedBy)

```
T1 (Repo Structure)
 |
 +---> T2 (Tauri + React + Vite) --+---> U1, U2, U3, U4, U5, U6 (UI)
 |                                  +---> TA1 (Rust commands)
 |                                  +---> TA2 (Python service comm)
 |                                  +---> TA3 (Image file mgmt)
 |
 +---> T3 (Python AI Service) -----+---> A1 (Plate detection model)
 |                                  +---> A5 (Detection API endpoint)
 |
 +---> T4 (Dev Environment Docs)    (can draft parallel w/ T2, T3)
 |
 +---> D1 (SQLite setup) ----------+---> D2 (Schema design) ---> D3 (Insert event) ---> D4 (Query events)
                                    +---> C5 (Camera persistence)

A1 (Plate detection) ---> A2 (OCR engine) ---> A3 (2-row plate) ---> A4 (Plate text cleanup)
A5 (Detection API) ------+-- blocked by A1, A2

C1 (RTSP connection) ---> C2 (Frame capture loop) ---> C3 (Stream to frontend)
C4 (Camera CRUD API) --- blocked by TA1 + D2

E1 (Detection trigger) --- blocked by A5 + C2
E2 (Snapshot capture) ---- blocked by E1 + TA3
E3 (Duplicate filtering) - blocked by E1 + D3
E4 (Event to frontend) --- blocked by E1 + U3

U1 (Camera dashboard) ---- blocked by T2 + C3
U3 (Detection panel) ----- blocked by T2 + E1
U4 (History table) -------- blocked by T2 + D4
U5 (Search bar) ----------- blocked by D4
U6 (Time filter) ---------- blocked by D4
```

---

## 2. Task Dependency Matrix

| Task | Depends On (BlockedBy) | Blocks | Sprint |
|------|----------------------|--------|--------|
| **T1** | - | T2, T3, T4, D1 | S1 |
| **T2** | T1 | U1-U6, TA1-TA3, C3, C4 | S1 |
| **T3** | T1 | A1, A5 | S1 |
| **T4** | T1, T2, T3 (partial) | - | S1-S2 |
| **D1** | T1 | D2, C5 | S1 |
| **D2** | D1 | D3, D4, C4, C5 | S1 |
| **D3** | D2 | E3 | S2 |
| **D4** | D2 | U4, U5, U6 | S2 |
| **C1** | T3 (OpenCV) | C2 | S2 |
| **C2** | C1 | C3, E1 | S2 |
| **C3** | C2, T2 | U1 | S3 |
| **C4** | TA1, D2 | U2 | S3 |
| **C5** | D2 | C4 | S2 |
| **A1** | T3 | A2, A5 | S2 |
| **A2** | A1 | A3, A5 | S2-S3 |
| **A3** | A2 | A4 | S3 |
| **A4** | A3 | - | S3 |
| **A5** | A1, A2 | E1 | S3 |
| **E1** | A5, C2 | E2, E3, E4, U3 | S4 |
| **E2** | E1, TA3 | - | S4 |
| **E3** | E1, D3 | - | S4 |
| **E4** | E1, U3 | - | S5 |
| **TA1** | T2 | C4 | S2 |
| **TA2** | T2, T3 | - | S2 |
| **TA3** | T2 | E2 | S2 |
| **U1** | T2, C3 | - | S4 |
| **U2** | T2, C4 | - | S4 |
| **U3** | T2, E1 | E4 | S4-S5 |
| **U4** | T2, D4 | - | S4 |
| **U5** | D4, U4 | - | S5 |
| **U6** | D4, U4 | - | S5 |

---

## 3. Sprint Plan (1 sprint = 1 week)

### Sprint 1 - Foundation (Week 1)
| Task | Description | Effort | Parallel? |
|------|------------|--------|-----------|
| T1 | Monorepo structure | 2 SP | First |
| T2 | Tauri + React + Vite init | 3 SP | After T1 |
| T3 | Python AI service init | 3 SP | Parallel w/ T2 |
| D1 | SQLite setup | 2 SP | After T1 |
| D2 | Schema design | 2 SP | After D1 |

**Deliverable:** Chay duoc `cargo tauri dev` + FastAPI `/health` + SQLite schema ready
**Critical Path:** T1 -> T2/T3 (parallel)

### Sprint 2 - Core Modules (Week 2)
| Task | Description | Effort | Parallel? |
|------|------------|--------|-----------|
| T4 | Dev environment docs | 2 SP | Background |
| TA1 | Rust commands bridge | 3 SP | - |
| TA2 | Python service comm | 3 SP | Parallel w/ TA1 |
| TA3 | Image file management | 2 SP | Parallel w/ TA1 |
| C1 | RTSP stream connection | 3 SP | Parallel track |
| C2 | Frame capture loop | 3 SP | After C1 |
| A1 | Plate detection model (YOLO) | 5 SP | Parallel track |
| D3 | Insert event | 1 SP | - |
| D4 | Query events | 2 SP | After D3 |
| C5 | Camera persistence | 2 SP | After D2 |

**Deliverable:** Rust-Python IPC working + RTSP frame capture + YOLO detect plate region
**Critical Path:** C1 -> C2, A1 (parallel heavy task)
**Note:** Sprint nang, co the overflow sang S3

### Sprint 3 - AI Pipeline + Integration (Week 3)
| Task | Description | Effort | Parallel? |
|------|------------|--------|-----------|
| A2 | OCR engine integration | 5 SP | - |
| A3 | 2-row plate handling | 3 SP | After A2 |
| A4 | Plate text cleanup | 2 SP | After A3 |
| A5 | Detection API endpoint | 3 SP | After A2 |
| C3 | Stream to frontend | 3 SP | Parallel |
| C4 | Camera CRUD API | 2 SP | Parallel |

**Deliverable:** Full AI pipeline: frame -> detect -> OCR -> plate text. Stream hien thi tren UI
**Critical Path:** A2 -> A3 -> A4, A5

### Sprint 4 - Event Processing + UI (Week 4)
| Task | Description | Effort | Parallel? |
|------|------------|--------|-----------|
| E1 | Detection trigger | 3 SP | - |
| E2 | Snapshot capture | 2 SP | After E1 |
| E3 | Duplicate filtering | 3 SP | After E1 |
| U1 | Camera dashboard | 5 SP | Parallel |
| U2 | Add camera dialog | 2 SP | Parallel |
| U3 | Detection panel | 3 SP | After E1 |
| U4 | History table | 3 SP | Parallel |

**Deliverable:** Detection event flow complete. Main UI screens functional
**Critical Path:** E1 -> E2/E3/U3

### Sprint 5 - Search + Polish (Week 5)
| Task | Description | Effort | Parallel? |
|------|------------|--------|-----------|
| E4 | Event to frontend (real-time) | 3 SP | - |
| U5 | Search bar | 2 SP | Parallel |
| U6 | Time filter | 2 SP | Parallel |
| - | Bug fixes & integration testing | 5 SP | - |

**Deliverable:** Search + filter working. Real-time event push to UI

### Sprint 6 - QA + Release (Week 6)
| Task | Description | Effort | Parallel? |
|------|------------|--------|-----------|
| - | End-to-end testing | 5 SP | - |
| - | Performance tuning (FPS, latency) | 3 SP | - |
| - | Build Windows installer | 2 SP | - |
| - | Documentation finalize | 2 SP | Parallel |

**Deliverable:** MVP release candidate

---

## 4. Critical Path

```
T1 -> T2 -> TA1 -> C4 -> U2
              |
T1 -> T3 -> A1 -> A2 -> A3 -> A4
              |     |
              |     +-> A5 -> E1 -> E2
              |                |-> E3
              |                |-> U3 -> E4
              |
T1 -> D1 -> D2 -> D3 -> E3
              |-> D4 -> U4 -> U5/U6
              |
     C1 -> C2 -> C3 -> U1
              |-> E1 (merge with A5)
```

**Longest path (critical):**
`T1 -> T3 -> A1 -> A2 -> A5 -> E1 -> U3 -> E4` (~6 weeks)

---

## 5. Risk & Bottleneck

| Risk | Impact | Sprint | Mitigation |
|------|--------|--------|-----------|
| A1+A2 (AI models) mat nhieu thoi gian tune | Delay S3-S4 | S2-S3 | Dung pre-trained model, khong fine-tune trong MVP |
| RTSP stream lag/crash | Block C2, C3 | S2 | Test som voi camera thuc, co fallback video file |
| Sprint 2 overloaded (10 tasks) | Overflow | S2 | Uu tien C1+A1 (critical path), doi T4 sang S3 |
| OCR accuracy VN plates thap | User rejection | S3 | Accept manual entry as fallback (Phase 2) |
| Tauri v2 breaking changes | Rework | S1 | Pin version, doc Tauri v2 migration guide |

---

## 6. Parallel Work Streams

| Stream | Tasks | Owner Focus |
|--------|-------|-------------|
| **Frontend** | T2 -> U1, U2, U3, U4, U5, U6 | React + Tauri UI |
| **AI/Python** | T3 -> A1, A2, A3, A4, A5 | YOLO + OCR pipeline |
| **Backend/Rust** | D1, D2, D3, D4, TA1, TA2, TA3 | SQLite + Rust commands |
| **Camera** | C1, C2, C3, C4, C5 | RTSP + OpenCV |
| **Events** | E1, E2, E3, E4 | Detection event flow |

**Ideal team size:** 2-3 devs co the lam parallel Frontend + AI + Backend streams

---

## 7. Current Status

| Task | Status | Notes |
|------|--------|-------|
| T1 | Pending | Jira ticket created, ready to start |
| T2 | Pending | Jira ticket created, blocked by T1 |
| T3 | Pending | Jira ticket created, blocked by T1 |
| T4 | Pending | Jira ticket created, blocked by T1/T2/T3 |
| All others | Not started | Awaiting Phase 1 setup completion |

**Next Action:** Start T1 (monorepo scaffold) -> unblock T2, T3, D1 for parallel work

---

## Unresolved Questions

1. Team size? 1 dev hay nhieu dev lam parallel? (anh huong timeline x2-x3 neu 1 dev)
2. Co camera thuc de test RTSP hay can mock/video file?
3. YOLO model nao? YOLOv8/v11 pre-trained hay custom train?
4. Sprint length chinh xac? 1 week hay 2 weeks?
5. Co CI/CD pipeline can setup trong Sprint 1 khong?
