# T4: Document Development Environment Setup

## SUMMARY

Create comprehensive dev environment documentation covering all required tools, versions, and setup steps for the LPR desktop app project.

## BACKGROUND / CONTEXT

- Project spans 3 tech stacks: Rust/Tauri, React/TypeScript/Vite, Python/FastAPI
- New developers need clear setup guide to onboard quickly
- Multiple OS-level dependencies (Rust toolchain, WebView2, OpenCV, Python) require explicit instructions
- Windows is the primary target platform

## SCOPE OF WORK

1. Create `docs/dev-setup-guide.md` with:
   - System requirements (OS, RAM, disk space)
   - Required tools with minimum versions
   - Step-by-step installation instructions per tool
   - Verification commands for each tool
2. Document required tools:
   - **Rust**: rustup, cargo, Tauri CLI (`cargo install tauri-cli`)
   - **Node.js**: v18+ with npm/pnpm
   - **Python**: 3.10+ with pip, venv
   - **OpenCV**: system-level or via pip (`opencv-python-headless`)
   - **WebView2**: Windows runtime (pre-installed on Win11, manual on Win10)
   - **Git**: version control
3. Document project-specific setup:
   - Clone repo
   - Install frontend deps: `npm install`
   - Set up Python venv: `cd ai-service && python -m venv venv && pip install -r requirements.txt`
   - First run: `cargo tauri dev`
4. Add troubleshooting section for common issues:
   - Rust build errors (missing C++ build tools)
   - WebView2 not found
   - Python venv activation on Windows (PowerShell vs cmd)
   - Port conflicts
5. Add quick-start commands summary table

## ACCEPTANCE CRITERIA

- [ ] A new developer can set up the project from scratch following only the doc
- [ ] All required tools listed with exact minimum versions
- [ ] Each tool has installation command and verification command
- [ ] Windows-specific instructions included (primary platform)
- [ ] Troubleshooting section covers top 5 common setup issues
- [ ] Quick-start summary table at top for experienced developers

## DEFINITION OF DONE

- [ ] `docs/dev-setup-guide.md` created and reviewed
- [ ] Verified by at least one team member following the guide on a clean machine
- [ ] Merged to main branch

## DEPENDENCIES

- **T1** (Repository structure) - docs folder must exist
- **T2** (Tauri + React init) - to verify frontend setup steps
- **T3** (Python AI service init) - to verify Python setup steps
- Can start drafting in parallel with T2/T3, finalize after they complete

## TECHNICAL NOTES

- Keep doc under 200 lines - link to external docs for detailed tool installation
- Use a version matrix table for quick reference:
  | Tool | Min Version | Install Command |
  |------|------------|-----------------|
  | Rust | 1.70+ | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
  | Node | 18+ | `nvm install 18` or download from nodejs.org |
  | Python | 3.10+ | Download from python.org |
  | Tauri CLI | 2.x | `cargo install tauri-cli` |
- Include `.env.example` if any env vars needed

## TESTING NOTES

- Validation: follow the guide on a clean Windows machine
- Check all verification commands produce expected output
- Ensure no steps are missing or out of order

## SUGGESTED LABELS

`documentation`, `setup`, `P0`, `phase-1`
