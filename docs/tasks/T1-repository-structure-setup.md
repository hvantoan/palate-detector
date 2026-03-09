# T1: Repository Structure Setup

**Priority:** P0 | **Sprint:** S1 | **Dependencies:** None

---

## SUMMARY

Initialize the monorepo directory structure with three main workspaces: `/src-tauri` (Rust backend), `/src` (React frontend), and `/ai-service` (Python AI service).

## BACKGROUND / CONTEXT

This is the foundational task for the License Plate Recognition desktop application. Before any development can begin, the repository must be organized as a monorepo to support the 3-tier architecture (Tauri/Rust + React + Python). Proper structure enables parallel development across frontend, backend, and AI teams.

## SCOPE OF WORK

1. Create root directory structure:
   - `/src-tauri/` - Tauri v2 Rust application
   - `/src/` - React + Vite frontend
   - `/ai-service/` - Python FastAPI service
2. Add root `package.json` for workspace management (optional npm workspaces)
3. Create `.gitignore` with entries for: `node_modules/`, `target/`, `__pycache__/`, `.venv/`, `*.pyc`, `.env`
4. Add root `README.md` with project overview and workspace links
5. Create placeholder `.gitkeep` files in empty directories
6. Initialize git repository (if not already)

## ACCEPTANCE CRITERIA

- [ ] Repository has `/src-tauri/`, `/src/`, `/ai-service/` directories
- [ ] Root `.gitignore` excludes all language-specific build artifacts
- [ ] Root `README.md` describes 3-tier architecture
- [ ] All directories committed to version control
- [ ] Structure matches documented architecture in PRD

## DEFINITION OF DONE

- Directory structure committed to `master` branch
- Code review approved (structure validation)
- README reflects actual project layout
- All developers can clone and verify structure

## DEPENDENCIES

None (foundational task)

## TECHNICAL NOTES

Monorepo pattern chosen for simpler dependency management and atomic commits across tiers. Consider using `pnpm` or `npm` workspaces if frontend shares packages with other JS components in future.

## TESTING NOTES

- Clone fresh copy of repo
- Verify all directories exist
- Verify `.gitignore` excludes test artifacts correctly

## SUGGESTED LABELS

`infrastructure`, `setup`, `priority-critical`, `sprint-1`