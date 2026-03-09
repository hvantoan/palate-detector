# C4: Camera CRUD API

**Priority:** P0 | **Sprint:** S3 | **BlockedBy:** TA1, D2

---

**TASK TITLE**
Implement Camera Management CRUD API in Rust Backend

**SUMMARY**
Create Tauri commands for camera lifecycle management: add, edit, delete, and list cameras with name and RTSP URL configuration.

**BACKGROUND / CONTEXT**
Users need to configure multiple IP cameras in the LPR system. A camera management API allows operators to add new cameras, update RTSP URLs when network changes, and remove decommissioned cameras. This API bridges the React UI to the SQLite database for camera persistence.

**SCOPE OF WORK**
- Define `Camera` struct in Rust: id, name, rtsp_url, created_at, updated_at, is_active
- Create Tauri command `add_camera(name: String, rtsp_url: String) -> Result<Camera, Error>`
- Create Tauri command `update_camera(id: i64, name: String, rtsp_url: String) -> Result<Camera, Error>`
- Create Tauri command `delete_camera(id: i64) -> Result<(), Error>`
- Create Tauri command `list_cameras() -> Result<Vec<Camera>, Error>`
- Create Tauri command `get_camera(id: i64) -> Result<Camera, Error>`
- Add RTSP URL validation (format check, not connectivity test)
- Return structured error responses for all failure cases
- Add logging for all CRUD operations

**ACCEPTANCE CRITERIA**
- `add_camera` creates new camera with auto-generated ID and timestamp
- `update_camera` modifies existing camera and updates `updated_at`
- `delete_camera` removes camera and returns success even if not found
- `list_cameras` returns all cameras ordered by created_at DESC
- Invalid RTSP URL format returns validation error with details
- Duplicate camera name returns conflict error
- All commands complete within 100ms for typical dataset (< 100 cameras)

**DEFINITION OF DONE**
- Rust commands implemented and unit tested
- Integration tests with Tauri invoke mock
- Error responses follow consistent JSON format
- API documented in project docs
- Frontend integration verified

**DEPENDENCIES**
- TA1: Rust commands infrastructure (must be complete)
- D2: Schema design with `cameras` table (must be complete)
- SQLite database initialized

**TECHNICAL NOTES**
Use `serde` for JSON serialization. Validate RTSP URL with regex: `^rtsp://.+:.+/.*`. Consider using `uuid` for camera IDs instead of auto-increment. Return `Result<T, ApiError>` pattern for consistent error handling.

**TESTING NOTES**
Test: add camera, add duplicate name, update non-existent camera, delete camera, list empty, list with data, invalid URL formats (http, ftp, empty), special characters in name.

**SUGGESTED LABELS**
backend, rust, tauri, camera, crud, api, P0, sprint-3