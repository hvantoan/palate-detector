# C3: Stream to Frontend

**Priority:** P0 | **Sprint:** S3 | **BlockedBy:** C2, T2

---

**TASK TITLE**
Implement Real-time Video Stream Delivery to React Frontend

**SUMMARY**
Create pipeline to send video frames from Python AI service / Rust backend to React UI for live camera display in the desktop application.

**BACKGROUND / CONTEXT**
Operators need to see live camera feeds in the desktop UI to monitor detection zones and verify system operation. Frames captured by C2 must be transmitted to the React frontend in real-time. This involves multiple components: Python capture -> Rust bridge -> Tauri event -> React component.

**SCOPE OF WORK**
- Create WebSocket or SSE endpoint in Rust backend for frame streaming
- Implement frame encoding (JPEG or WebP) for efficient transfer
- Create Tauri event emission for frame broadcast to frontend
- Build React component `LiveCameraView` to display frames
- Implement frame rate limiting for UI (target: 15-30 FPS display)
- Add connection status indicator in UI (connected/connecting/error)
- Create full-screen mode for camera view
- Handle multiple camera streams with camera ID routing

**ACCEPTANCE CRITERIA**
- Live video displayed in UI with < 500ms latency
- UI displays "Connecting..." state while establishing stream
- Connection status updates in real-time (green/yellow/red indicator)
- Full-screen mode available via click or button
- Frame encoding produces images < 100KB each
- Multiple camera views switchable without reconnect
- Graceful degradation when bandwidth limited

**DEFINITION OF DONE**
- Code implemented across Python/Rust/React layers
- E2E test with real camera or mock stream
- UI review approved by product/design
- Latency measured and documented
- Browser DevTools shows acceptable memory usage

**DEPENDENCIES**
- C2: Frame capture loop (must be complete)
- T2: Tauri + React + Vite init (must be complete)
- Tauri event system configured
- Rust-Python communication established

**TECHNICAL NOTES**
Prefer Tauri events over WebSocket for desktop app (no network overhead). Encode frames as JPEG (quality 70-80) for balance of size/quality. Use React `useEffect` with cleanup for subscription management.

**TESTING NOTES**
Test: stream latency, UI reconnection after backend restart, memory leak in frontend during 1-hour stream, rapid camera switching, full-screen toggle, network-simulated latency.

**SUGGESTED LABELS**
frontend, backend, camera, streaming, tauri, react, P0, sprint-3