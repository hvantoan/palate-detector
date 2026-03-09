# T4: Document Development Environment Setup

**Priority:** P0 | **Sprint:** S1-S2 | **Dependencies:** T1, T2, T3

---

## SUMMARY

Create comprehensive documentation for setting up the complete development environment including Rust, Node.js, Python, OpenCV, and platform-specific build tools for Tauri.

## BACKGROUND / CONTEXT

Developers need clear, verified instructions to set up their local environment for the 3-tier application. Without proper documentation, onboarding becomes time-consuming and error-prone. This documentation serves as the single source of truth for environment requirements.

## SCOPE OF WORK

1. Create `/docs/dev-setup-guide.md` with sections:
   - Prerequisites (OS, hardware requirements)
   - Windows setup (primary platform)
   - Rust installation and verification
   - Node.js installation and verification
   - Python installation and virtual environment setup
   - Tauri prerequisites (WebView2, Visual Studio Build Tools)
   - OpenCV setup for Python
   - IDE recommendations (VS Code extensions)
   - Verification checklist (commands to verify each tool)
2. Add installation commands for each platform:
   - Windows (winget, chocolatey, or manual)
   - Linux (apt, dnf - secondary support)
   - macOS (brew - secondary support)
3. Include version requirements table:
   - Node.js 18+ LTS
   - Rust 1.70+
   - Python 3.10+
4. Add troubleshooting section for common issues
5. Create `scripts/verify-env.sh` (or `.ps1`) to check all dependencies
6. Update root `README.md` with link to setup guide
7. Document how to run each workspace:
   - Frontend: `npm run tauri dev`
   - AI Service: `python run.py`

## ACCEPTANCE CRITERIA

- [ ] Setup guide covers all required tools with version requirements
- [ ] Windows installation instructions verified on clean machine
- [ ] Each tool has "verify" command (e.g., `node --version`)
- [ ] Troubleshooting section includes at least 3 common issues
- [ ] Verification script runs and reports missing tools
- [ ] Root README links to setup guide
- [ ] Guide explains how to run each tier (frontend, backend, AI)

## DEFINITION OF DONE

- Documentation reviewed by at least one other developer
- Setup guide tested by following steps on fresh environment
- All links and commands verified working
- Merged to master branch
- Accessible from root README

## DEPENDENCIES

- T1, T2, T3 (all project structure and initialization must be complete to document actual commands)

## TECHNICAL NOTES

Focus on Windows as primary platform per PRD. Use winget commands where possible for Windows. Include WebView2 installation link (required for Tauri on Windows). Note that OpenCV Python wheels include binaries, no separate install needed on most systems.

## TESTING NOTES

- Have a developer follow the guide on a fresh machine
- Verify all version commands work
- Run verification script
- Verify `npm run tauri dev` works after full setup
- Verify AI service starts after Python setup

## SUGGESTED LABELS

`documentation`, `onboarding`, `setup`, `priority-critical`, `sprint-1`, `sprint-2`