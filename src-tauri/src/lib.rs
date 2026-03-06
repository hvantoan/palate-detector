// Palate Detector - License Plate Recognition Desktop App
// Shared library module for Tauri v2 backend

// Learn more about Tauri commands at https://tauri.app/develop/calling-rust/

/// Run the Tauri application
///
/// This function initializes and runs the Tauri application.
/// It sets up the shell plugin for executing external commands.
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}