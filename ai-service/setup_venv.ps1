#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Sets up the Python virtual environment for the AI Service.

.DESCRIPTION
    This script creates a Python virtual environment, activates it,
    and installs all required dependencies from requirements.txt.

.PARAMETER PythonPath
    Optional path to Python executable. Defaults to 'python' (uses system PATH).

.PARAMETER VenvName
    Name of the virtual environment directory. Defaults to '.venv'.

.PARAMETER SkipInstall
    Skip pip install step (only create/activate venv).

.EXAMPLE
    .\setup_venv.ps1
    Creates .venv and installs all dependencies.

.EXAMPLE
    .\setup_venv.ps1 -PythonPath "C:\Python310\python.exe"
    Uses specific Python version for venv creation.

.EXAMPLE
    .\setup_venv.ps1 -SkipInstall
    Creates .venv without installing dependencies.

.NOTES
    File Name      : setup_venv.ps1
    Prerequisite   : Python 3.10+
    Copyright 2026 - Palate Detector AI Service
#>

param(
    [string]$PythonPath = "python",
    [string]$VenvName = ".venv",
    [switch]$SkipInstall
)

$ErrorActionPreference = "Stop"

# ============================================
# HELPER FUNCTIONS
# ============================================

function Write-Step {
    param([string]$Message)
    Write-Host "`n>>> $Message" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "    [OK] $Message" -ForegroundColor Green
}

function Write-Error-Step {
    param([string]$Message)
    Write-Host "    [ERROR] $Message" -ForegroundColor Red
}

function Test-PythonVersion {
    param([string]$PythonExe)

    try {
        $versionOutput = & $PythonExe --version 2>&1
        if ($versionOutput -match "Python (\d+)\.(\d+)") {
            $major = [int]$Matches[1]
            $minor = [int]$Matches[2]

            if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 10)) {
                Write-Error-Step "Python 3.10+ required. Found: $versionOutput"
                return $false
            }
            return $true
        }
    } catch {
        Write-Error-Step "Could not determine Python version"
        return $false
    }
    return $false
}

# ============================================
# MAIN SCRIPT
# ============================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "AI Service - Virtual Environment Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Step 1: Check Python
Write-Step "Checking Python installation..."

if (-not (Get-Command $PythonPath -ErrorAction SilentlyContinue)) {
    Write-Error-Step "Python not found at: $PythonPath"
    Write-Host "`nPlease install Python 3.10+ or specify path with -PythonPath" -ForegroundColor Yellow
    exit 1
}

if (-not (Test-PythonVersion -PythonExe $PythonPath)) {
    exit 1
}

$pythonVersion = & $PythonPath --version 2>&1
Write-Success "Found $pythonVersion"

# Step 2: Create virtual environment
Write-Step "Creating virtual environment..."

if (Test-Path $VenvName) {
    Write-Host "    Virtual environment '$VenvName' already exists." -ForegroundColor Yellow
    $response = Read-Host "    Recreate? (y/N)"
    if ($response -eq "y" -or $response -eq "Y") {
        Remove-Item -Recurse -Force $VenvName
        & $PythonPath -m venv $VenvName
        if ($LASTEXITCODE -ne 0) {
            Write-Error-Step "Failed to create virtual environment"
            exit 1
        }
        Write-Success "Virtual environment recreated"
    } else {
        Write-Success "Using existing virtual environment"
    }
} else {
    & $PythonPath -m venv $VenvName
    if ($LASTEXITCODE -ne 0) {
        Write-Error-Step "Failed to create virtual environment"
        exit 1
    }
    Write-Success "Virtual environment created at: $VenvName"
}

# Step 3: Activate virtual environment
Write-Step "Activating virtual environment..."

$activateScript = Join-Path $VenvName "Scripts\Activate.ps1"

if (-not (Test-Path $activateScript)) {
    Write-Error-Step "Activation script not found: $activateScript"
    exit 1
}

& $activateScript
Write-Success "Virtual environment activated"

# Step 4: Upgrade pip
Write-Step "Upgrading pip..."

& python -m pip install --upgrade pip --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host "    [WARN] Could not upgrade pip (non-critical)" -ForegroundColor Yellow
} else {
    Write-Success "pip upgraded to latest version"
}

# Step 5: Install dependencies
if (-not $SkipInstall) {
    Write-Step "Installing dependencies from requirements.txt..."

    if (-not (Test-Path "requirements.txt")) {
        Write-Error-Step "requirements.txt not found"
        exit 1
    }

    & pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Error-Step "Failed to install dependencies"
        exit 1
    }
    Write-Success "All dependencies installed"
} else {
    Write-Host "    Skipping dependency installation (-SkipInstall)" -ForegroundColor Yellow
}

# ============================================
# SUMMARY
# ============================================

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan

Write-Host "`nNext steps:" -ForegroundColor White
Write-Host "  1. Activate the virtual environment:" -ForegroundColor White
Write-Host "     .\$VenvName\Scripts\Activate.ps1" -ForegroundColor Gray
Write-Host ""
Write-Host "  2. Run the server:" -ForegroundColor White
Write-Host "     python run.py" -ForegroundColor Gray
Write-Host ""
Write-Host "  3. Or use uvicorn directly:" -ForegroundColor White
Write-Host "     uvicorn main:app --host 0.0.0.0 --port 8100 --reload" -ForegroundColor Gray
Write-Host ""
Write-Host "API endpoints:" -ForegroundColor White
Write-Host "  Health:    http://localhost:8100/health" -ForegroundColor Green
Write-Host "  Detection: http://localhost:8100/detect/" -ForegroundColor Green
Write-Host "  Swagger:   http://localhost:8100/docs" -ForegroundColor Green
Write-Host "  ReDoc:     http://localhost:8100/redoc" -ForegroundColor Green
Write-Host ""