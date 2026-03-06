// Prevents additional console window on Windows in release builds
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    // Placeholder: Tauri application entry point
    // Actual Tauri initialization will be in lib.rs
    palate_detector_lib::run()
}