# C2: Frame Capture Loop

**Priority:** P0 | **Sprint:** S2 | **BlockedBy:** C1

---

**TASK TITLE**
Implement Frame Capture Loop for RTSP Stream Processing

**SUMMARY**
Create continuous frame capture mechanism from connected RTSP stream at configurable 5-10 FPS for license plate detection processing.

**BACKGROUND / CONTEXT**
After establishing RTSP connection (C1), the system needs a frame capture loop to extract video frames at a controlled rate. The 5-10 FPS target balances detection accuracy with CPU/memory efficiency. Higher FPS would not significantly improve detection quality while consuming more resources.

**SCOPE OF WORK**
- Create `FrameCapture` class extending `CameraStream`
- Implement configurable FPS setting (default: 7 FPS, range: 5-10)
- Add frame buffer queue (max 3 frames) for downstream processing
- Implement frame capture in separate thread to avoid blocking
- Add frame timestamp metadata for each captured frame
- Create frame drop handling when queue is full
- Expose `get_frame()` method for AI pipeline consumption
- Add metrics: frames captured, frames dropped, current FPS

**ACCEPTANCE CRITERIA**
- Frames captured at configured FPS (±1 FPS tolerance)
- Each frame includes timestamp and source camera ID
- Frame queue does not exceed max buffer size
- Dropped frames are logged with reason
- `get_frame()` returns latest frame within 100ms
- FPS can be adjusted at runtime without reconnect
- Memory usage stable during 1-hour continuous capture test

**DEFINITION OF DONE**
- Code implemented and reviewed
- Unit tests for frame capture and queue behavior
- Performance test showing stable memory over 1 hour
- FPS accuracy verified with timing logs
- Code merged to main branch

**DEPENDENCIES**
- C1: RTSP stream connection (must be complete)
- Python threading/multiprocessing module
- Frame storage strategy (in-memory queue)

**TECHNICAL NOTES**
Use `threading.Thread` with daemon=True for automatic cleanup. Implement `time.sleep()` between captures for FPS control. Consider using `queue.Queue` for thread-safe frame buffer. Frame format: BGR numpy array (OpenCV default).

**TESTING NOTES**
Test: FPS accuracy (measure actual vs configured), frame queue overflow, consumer slower than producer, rapid FPS changes, stream disconnect during capture, memory leak over extended run.

**SUGGESTED LABELS**
backend, camera, python, streaming, performance, P0, sprint-2