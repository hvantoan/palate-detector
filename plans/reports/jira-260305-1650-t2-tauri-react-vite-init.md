# T2: Initialize Tauri v2 Project with React + Vite Frontend

## SUMMARY

Scaffold a Tauri v2 desktop application using React + Vite as the frontend framework. This establishes the core development shell that all subsequent UI and Rust backend tasks build upon.

## BACKGROUND / CONTEXT

- Foundational setup task for the License Plate Recognition (LPR) desktop app
- Tauri v2 for native desktop capabilities (SQLite, filesystem, system tray) with React + Vite frontend
- All subsequent tasks (Camera module, UI, Tauri integration) depend on this scaffold
- Tauri v2 chosen for lightweight binaries, native Rust backend, cross-platform potential (Windows primary)

## SCOPE OF WORK

1. Initialize Tauri v2 project using `create-tauri-app` with React + Vite template
2. Configure project structure following monorepo layout:
   - `/src` - React frontend (Vite)
   - `/src-tauri` - Rust backend (Tauri)
3. Set up Vite config with dev server settings (port, HMR proxy for Tauri)
4. Configure `tauri.conf.json`:
   - App identifier, window title, default window size
   - Allowed Tauri APIs (fs, shell, dialog, etc.)
   - Dev server URL pointing to Vite
5. Set up TypeScript config for React + Tauri type bindings
6. Add frontend dependencies: `react`, `react-dom`, `@tauri-apps/api`
7. Add Rust dependencies in `Cargo.toml`: `tauri`, `serde`, `serde_json`
8. Create minimal "Hello World" React page that invokes a Tauri command (verify IPC works)
9. Verify `cargo tauri dev` launches app with hot-reload working
10. Verify `cargo tauri build` produces a debug binary without errors

## ACCEPTANCE CRITERIA

- [ ] `npm run tauri dev` launches a native desktop window with React UI
- [ ] Vite HMR works - changing React code reflects instantly in the app
- [ ] A sample Tauri command (e.g., `greet`) invoked from React returns a response
- [ ] Project compiles without errors on Windows
- [ ] Frontend files in `/src`, Rust files in `/src-tauri`
- [ ] `tauri.conf.json` has correct app identifier (e.g., `com.vif.palate-detector`)
- [ ] TypeScript compiles without type errors
- [ ] No unused boilerplate/template code left in the project

## DEFINITION OF DONE

- [ ] Project scaffolded and committed to repository
- [ ] `cargo tauri dev` runs successfully
- [ ] `cargo tauri build` compiles without errors
- [ ] Dev docs updated with setup instructions (required tools, versions)
- [ ] Code reviewed and merged to main branch

## DEPENDENCIES

- **T1** (Repository structure) - must be completed first
- Required tooling: Rust toolchain (stable), Node.js (v18+), npm/pnpm
- Tauri v2 prerequisites: WebView2 (Windows)

## TECHNICAL NOTES

- Use Tauri v2 (not v1) - improved plugin system, better security model
- Keep Vite config minimal - no unnecessary plugins (YAGNI)
- Set `"build.devUrl"` in tauri.conf.json to match Vite dev server (default `http://localhost:5173`)
- Set `"build.beforeDevCommand": "npm run dev"` and `"build.beforeBuildCommand": "npm run build"`

## TESTING NOTES

- Manual: `cargo tauri dev` launches window, React UI renders
- Manual: modify React component -> verify HMR updates without restart
- Manual: click button calling Tauri command -> verify response displayed
- Manual: `cargo tauri build` -> verify `.exe` in `src-tauri/target/release`

## SUGGESTED LABELS

`setup`, `frontend`, `P0`, `phase-1`, `tauri`, `react`
