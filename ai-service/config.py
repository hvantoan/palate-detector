"""
Configuration settings for the AI Service.

Uses pydantic-settings for environment variable support.
All settings can be overridden via environment variables.
"""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration settings.

    All settings can be overridden via environment variables.
    Example: PORT=9000 python run.py
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Server Configuration
    host: str = Field(
        default="0.0.0.0",
        description="Host address to bind the server",
    )
    port: int = Field(
        default=8100,
        ge=1,
        le=65535,
        description="Port to bind the server (default: 8100 to avoid common dev ports)",
    )
    reload: bool = Field(
        default=False,
        description="Enable auto-reload for development",
    )

    # Model Configuration
    models_dir: Path = Field(
        default=Path("models"),
        description="Directory containing model files",
    )
    yolo_model_path: Path = Field(
        default=Path("models/yolo_plate_detection.pt"),
        description="Path to YOLO plate detection model",
    )
    ocr_model_path: Path = Field(
        default=Path("models/ocr"),
        description="Path to OCR model directory",
    )

    # Detection Thresholds
    confidence_threshold: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="Minimum confidence score for plate detection",
    )
    nms_threshold: float = Field(
        default=0.4,
        ge=0.0,
        le=1.0,
        description="Non-maximum suppression threshold for overlapping detections",
    )
    min_plate_area: int = Field(
        default=500,
        ge=0,
        description="Minimum area (pixels) for valid plate detection",
    )

    # Upload Configuration
    max_upload_size: int = Field(
        default=10 * 1024 * 1024,  # 10MB
        ge=1,
        description="Maximum file upload size in bytes",
    )
    allowed_image_types: list[str] = Field(
        default=["image/jpeg", "image/png", "image/webp"],
        description="Allowed MIME types for image uploads",
    )

    # Logging Configuration
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO",
        description="Logging level",
    )

    # CORS Configuration
    cors_origins: list[str] = Field(
        default=["tauri://localhost", "http://localhost"],
        description="Allowed CORS origins",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Get cached application settings.

    Uses lru_cache to ensure settings are only loaded once.

    Returns:
        Settings: Application configuration instance
    """
    return Settings()


# Convenience export for direct access
settings = get_settings()