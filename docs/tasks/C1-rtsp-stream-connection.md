# C1: RTSP Stream Connection

**Priority:** P0 | **Sprint:** S2 | **BlockedBy:** T3

---

**TASK TITLE**
Implement RTSP Stream Connection for IP Camera Integration

**SUMMARY**
Establish connection to IP cameras via RTSP URL using OpenCV in Python AI service to enable video frame acquisition.

**BACKGROUND / CONTEXT**
The LPR (License Plate Recognition) system needs to connect to IP cameras to capture video streams for plate detection. This is a foundational component of the Camera Module that enables all downstream processing (frame capture, AI detection, event creation). Without RTSP connectivity, the system cannot receive video input from security cameras.

**SCOPE OF WORK**
- Install OpenCV Python package with FFmpeg support in ai-service
- Create `CameraStream` class in `ai-service/src/camera/` module
- Implement RTSP connection handler with URL validation
- Add connection timeout handling (default 10s)
- Implement reconnection logic on connection drop
- Create health check endpoint to verify stream status
- Add logging for connection events (connect, disconnect, error)
- Handle authentication for RTSP URLs with username/password

**ACCEPTANCE CRITERIA**
- Given valid RTSP URL, connection established within 10 seconds
- Invalid RTSP URL returns descriptive error (not found, auth failed, timeout)
- Connection auto-reconnects after network interruption
- Health check endpoint returns current stream status
- Logs capture all connection state changes with timestamps
- Supports RTSP URLs with embedded credentials (rtsp://user:pass@host:port/path)

**DEFINITION OF DONE**
- Code implemented and reviewed
- Unit tests for connection success/failure scenarios
- Integration test with mock RTSP server
- Documentation added to ai-service README
- Tested with at least one real IP camera model

**DEPENDENCIES**
- T3: Python AI service init (must be complete)
- OpenCV Python package installed
- Test IP camera or mock RTSP server for validation

**TECHNICAL NOTES**
Use OpenCV VideoCapture with CAP_FFMPEG backend. Consider using `cv2.CAP_PROP_BUFFERSIZE` to control buffer. Store connection state in class instance for health checks.

**TESTING NOTES**
Test: valid/invalid URL, authenticated URL, connection timeout, network drop during stream, multiple sequential connections to same URL, concurrent connections to different URLs.

**SUGGESTED LABELS**
backend, camera, python, rtsp, opencv, P0, sprint-2