"""
Detection service for license plate recognition.

This module provides the core detection logic for identifying
and extracting license plate information from images.

Current implementation uses mock data. Future versions will
integrate YOLO model for plate detection and OCR for text recognition.
"""

import logging
from typing import BinaryIO

from config import settings
from models.schemas import DetectionResponse, PlateDetection

logger = logging.getLogger(__name__)


class DetectionError(Exception):
    """Base exception for detection-related errors."""

    pass


class FileTooLargeError(DetectionError):
    """Raised when uploaded file exceeds maximum size limit."""

    def __init__(self, size: int, max_size: int) -> None:
        self.size = size
        self.max_size = max_size
        super().__init__(
            f"File size ({size} bytes) exceeds maximum allowed ({max_size} bytes)"
        )


class InvalidImageError(DetectionError):
    """Raised when the provided file is not a valid image."""

    pass


def validate_image_size(size: int) -> None:
    """
    Validate that the image size is within acceptable limits.

    Args:
        size: Size of the image in bytes.

    Raises:
        FileTooLargeError: If size exceeds maximum upload size.
    """
    if size > settings.max_upload_size:
        raise FileTooLargeError(size, settings.max_upload_size)


def detect_plates(image_data: bytes | BinaryIO) -> DetectionResponse:
    """
    Detect license plates in an image.

    This is a mock implementation that returns fixed plate data.
    Future versions will use YOLO for plate detection and OCR
    for text recognition.

    Args:
        image_data: Raw image bytes or file-like object.

    Returns:
        DetectionResponse: List of detected plates with text,
            confidence scores, and bounding boxes.

    Raises:
        FileTooLargeError: If image exceeds maximum size.
        InvalidImageError: If image cannot be processed.

    Example:
        >>> with open("car.jpg", "rb") as f:
        ...     response = detect_plates(f.read())
        >>> for plate in response.plates:
        ...     print(f"Found: {plate.plate_text} ({plate.confidence:.2%})")
    """
    # Handle both bytes and file-like objects
    if hasattr(image_data, "read"):
        # It's a file-like object, read the content
        if hasattr(image_data, "seek"):
            image_data.seek(0)
        content = image_data.read()
        if isinstance(content, str):
            content = content.encode("utf-8")
        image_bytes = content
    else:
        image_bytes = image_data

    # Validate size
    validate_image_size(len(image_bytes))

    # Validate minimum image size (trivial check for empty/invalid data)
    if len(image_bytes) < 100:
        raise InvalidImageError("Image data too small to be valid")

    # Log detection request
    logger.info(
        "Processing detection request",
        extra={
            "image_size": len(image_bytes),
            "confidence_threshold": settings.confidence_threshold,
        },
    )

    # Mock detection: Return fixed plate data
    # In production, this would:
    # 1. Decode image with OpenCV
    # 2. Run YOLO detection for plate localization
    # 3. Crop detected regions
    # 4. Run OCR on cropped plates
    # 5. Filter results by confidence threshold

    mock_plates = [
        PlateDetection(
            plate_text="51F-123.45",
            confidence=0.95,
            bbox=[100, 100, 300, 150],
        ),
    ]

    # Filter by confidence threshold
    filtered_plates = [
        plate
        for plate in mock_plates
        if plate.confidence >= settings.confidence_threshold
    ]

    logger.info(
        "Detection complete",
        extra={
            "plates_found": len(filtered_plates),
        },
    )

    return DetectionResponse(plates=filtered_plates)