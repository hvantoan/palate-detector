# C5: Camera Persistence

**Priority:** P0 | **Sprint:** S2 | **BlockedBy:** D2

---

**TASK TITLE**
Implement Camera Configuration Persistence with SQLite

**SUMMARY**
Create database layer for storing and retrieving camera configurations in SQLite, enabling camera settings to persist across application restarts.

**BACKGROUND / CONTEXT**
Camera configurations must survive application restarts and be available immediately on startup. SQLite provides a lightweight, file-based database suitable for desktop applications. The `cameras` table stores essential camera metadata including name, RTSP URL, and timestamps.

**SCOPE OF WORK**
- Define `cameras` table schema in migration file
- Implement `CameraRepository` struct with SQLite connection
- Create `insert_camera(camera: Camera) -> Result<i64, Error>` method
- Create `find_camera_by_id(id: i64) -> Result<Option<Camera>, Error>` method
- Create `find_all_cameras() -> Result<Vec<Camera>, Error>` method
- Create `update_camera(camera: Camera) -> Result<(), Error>` method
- Create `delete_camera(id: i64) -> Result<(), Error>` method
- Add database migration on app startup
- Create seed data option for development/testing
- Add database backup method for user data export

**ACCEPTANCE CRITERIA**
- Camera data persists after application restart
- Schema migration runs automatically on app launch
- All CRUD operations return within 50ms for < 100 cameras
- Database file created in platform-appropriate location (AppData on Windows)
- Corrupted database shows user-friendly error message
- Backup creates restorable database snapshot

**DEFINITION OF DONE**
- Repository implemented with full CRUD
- Migration tested with fresh and existing databases
- Database file location documented
- Backup/restore functionality verified
- Performance benchmarks documented

**DEPENDENCIES**
- D2: Schema design (must be complete)
- SQLite library configured in Rust (rusqlite or diesel)
- Tauri app data directory configured

**TECHNICAL NOTES**
Use `rusqlite` crate for lightweight SQLite access. Store database at `{app_data_dir}/lpr.db`. Use `CREATE TABLE IF NOT EXISTS` for idempotent migration. Consider WAL mode for better concurrent read/write performance.

**TESTING NOTES**
Test: insert and retrieve, update and verify, delete and verify empty, app restart preserves data, corrupted database handling, large dataset performance (1000+ cameras), concurrent read/write operations.

**SUGGESTED LABELS**
backend, rust, database, sqlite, persistence, camera, P0, sprint-2