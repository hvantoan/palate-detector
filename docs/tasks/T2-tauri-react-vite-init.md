# T2: Initialize Tauri v2 with React + Vite Frontend

**Priority:** P0 | **Sprint:** S1 | **Dependencies:** T1

---

## SUMMARY

Set up the desktop application framework using Tauri v2 with React frontend and Vite build tooling, enabling cross-platform desktop development.

## BACKGROUND / CONTEXT

Tauri v2 is the core desktop framework that bridges Rust backend with React frontend. This task creates the foundational shell for the license plate recognition app UI and native OS integration. React + Vite provides fast HMR and optimized production builds.

## SCOPE OF WORK

1. Run `npm create tauri-app@latest` with React + TypeScript template
2. Configure `src-tauri/tauri.conf.json`:
   - Set app identifier (e.g., `com.palate-detector.app`)
   - Configure window settings (size, title, decorations)
   - Set build targets (Windows primary)
3. Configure Vite in `vite.config.ts`:
   - Set up React plugin
   - Configure path aliases (`@/` for `src/`)
   - Set up dev server port
4. Add base frontend dependencies:
   - `react-router-dom` (routing)
   - `@tauri-apps/api` (Tauri JS API)
5. Create basic folder structure in `/src`:
   - `components/`, `pages/`, `hooks/`, `utils/`, `styles/`
6. Add `src-tauri/Cargo.toml` dependencies preview (not full implementation)
7. Create `src/App.tsx` with basic layout placeholder
8. Verify dev server runs: `npm run tauri dev`

## ACCEPTANCE CRITERIA

- [ ] `npm run tauri dev` launches desktop window with React app
- [ ] Hot module replacement works for React components
- [ ] TypeScript compilation succeeds with no errors
- [ ] Tauri config has correct app identifier and window settings
- [ ] Basic folder structure follows PRD architecture
- [ ] Build command `npm run tauri build` completes without errors

## DEFINITION OF DONE

- Tauri v2 + React + Vite project committed
- Dev environment verified on at least one developer machine
- README in `/src` with setup instructions
- PR with initialization verified and merged

## DEPENDENCIES

- T1 (Repository structure must exist)

## TECHNICAL NOTES

Tauri v2 uses different configuration format than v1. Use `@tauri-apps/api` v2.x. Window size should be at least 1280x720 for dashboard UI. Enable devtools in development mode for debugging.

## TESTING NOTES

- Run `npm run tauri dev` - verify window opens
- Make a change to `App.tsx` - verify HMR
- Run `npm run tauri build` - verify binary created
- Check TypeScript: `npm run type-check` (if configured)

## SUGGESTED LABELS

`frontend`, `tauri`, `react`, `setup`, `priority-critical`, `sprint-1`