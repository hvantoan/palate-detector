# Development Environment Setup Guide

Quick reference for setting up the Palate Detector LPR desktop application development environment.

## Quick-Start Summary

| Tool | Min Version | Verify Command | Download |
|------|-------------|----------------|----------|
| Node.js | 18.x LTS | `node --version` | [nodejs.org](https://nodejs.org/) |
| Rust | 1.70+ | `rustc --version` | [rust-lang.org](https://www.rust-lang.org/tools/install) |
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| Tauri CLI | 2.x | `npm list @tauri-apps/cli` | Installed via npm |
| WebView2 | Evergreen | N/A | [WebView2](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) |

**Ports:** Frontend (5173) | AI Service (8100)

---

## System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| OS | Windows 10 64-bit | Windows 11 |
| RAM | 8 GB | 16 GB |
| Disk | 5 GB | 10 GB |

---

## Tool Installation

### Node.js (18+ LTS)
```powershell
winget install OpenJS.NodeJS.LTS
node --version      # Expected: v18.x.x+
```

### Rust (1.70+)
```powershell
winget install Rustlang.Rustup
# Restart terminal
rustc --version     # Expected: 1.70.0+
```

### Python (3.10+)
```powershell
winget install Python.Python.3.12
# Check "Add Python to PATH" during install
python --version    # Expected: 3.10.x+
```

### Tauri CLI (2.x)
```powershell
npm install -g @tauri-apps/cli
tauri --version     # Expected: 2.x.x
```

### WebView2 (Windows)
Pre-installed on Windows 10/11. If missing: [Download WebView2 Bootstrapper](https://developer.microsoft.com/en-us/microsoft-edge/webview2/#download-section)

---

## Project Setup

### 1. Clone & Install
```powershell
git clone <repository-url>
cd palate-detector
npm install

# Frontend dependencies
cd src && npm install && cd ..

# Python AI Service
cd ai-service
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd ..
```

### 2. Run Development
```powershell
# Terminal 1: AI Service
cd ai-service && .\.venv\Scripts\Activate.ps1 && python run.py

# Terminal 2: Tauri App
npm run tauri:dev
```

---

## Troubleshooting

### 1. Rust Build Errors
**Symptom:** `linker 'link.exe' not found`
```powershell
winget install Microsoft.VisualStudio.2022.BuildTools
# Select "Desktop development with C++" workload
```

### 2. WebView2 Not Found
**Symptom:** `WebView2Loader.dll not found`
```powershell
winget install Microsoft.EdgeWebView2Runtime
```

### 3. PowerShell Venv Activation Failed
**Symptom:** `Activate.ps1 cannot be loaded`
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

### 4. Port Conflicts
**Symptom:** `Address already in use`
```powershell
netstat -ano | findstr :5173    # Check frontend port
netstat -ano | findstr :8100    # Check AI service port
taskkill /PID <PID> /F          # Kill process
$env:PORT=8200; python run.py   # Use different port
```

### 5. OpenCV Installation Issues
**Symptom:** `pip install opencv-python` fails
```powershell
pip install opencv-python-headless
python -c "import cv2; print(cv2.__version__)"  # Verify
```

---

## Useful Commands

| Task | Command |
|------|---------|
| Start dev | `npm run tauri:dev` |
| Build | `npm run tauri:build` |
| AI service | `cd ai-service && python run.py` |
| Frontend only | `npm run dev` |

---

## External Resources

- [Tauri Docs](https://tauri.app/v2/guide/)
- [Rust Installation](https://www.rust-lang.org/tools/install)
- [Node.js Downloads](https://nodejs.org/en/download/)
- [Python Downloads](https://www.python.org/downloads/)
- [WebView2 Docs](https://docs.microsoft.com/en-us/microsoft-edge/webview2/)