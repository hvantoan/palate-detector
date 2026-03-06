"""
Detection API router for license plate recognition.

Provides endpoints for uploading images and receiving
license plate detection results.
"""

import logging
from typing import Annotated

from fastapi import APIRouter, File, HTTPException, UploadFile

from models.schemas import DetectionResponse
from services.detection import (
    DetectionError,
    FileTooLargeError,
    InvalidImageError,
    detect_plates,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/detect", tags=["detection"])


@router.post(
    "/",
    response_model=DetectionResponse,
    summary="Detect license plates in an image",
    description="""
Upload an image file to detect license plates.

Returns a list of detected plates with:
- **plate_text**: The recognized text from the license plate
- **confidence**: Detection confidence score (0.0 to 1.0)
- **bbox**: Bounding box coordinates [x1, y1, x2, y2]

Supported image formats: JPEG, PNG, WebP
Maximum file size: 10MB
    """,
    responses={
        200: {
            "description": "Successfully processed image",
            "content": {
                "application/json": {
                    "example": {
                        "plates": [
                            {
                                "plate_text": "51F-123.45",
                                "confidence": 0.95,
                                "bbox": [100, 100, 300, 150],
                            }
                        ]
                    }
                }
            },
        },
        400: {
            "description": "Bad request - invalid or empty image file",
            "content": {
                "application/json": {
                    "examples": {
                        "empty_file": {"summary": "Empty file", "value": {"detail": "Empty file uploaded"}},
                        "invalid_image": {
                            "summary": "Invalid image",
                            "value": {"detail": "Invalid image data too small to be valid"},
                        },
                        "file_too_large": {
                            "summary": "File too large",
                            "value": {"detail": "File size (15000000 bytes) exceeds maximum allowed (10000000 bytes)"},
                        },
                    }
                }
            },
        },
    },
)
async def detect(
    file: Annotated[
        UploadFile,
        File(
            description="Image file to process. Supported formats: JPEG, PNG, WebP. Max size: 10MB"
        ),
    ],
) -> DetectionResponse:
    """
    Detect license plates in an uploaded image.

    This endpoint accepts multipart/form-data uploads and returns
    detection results containing plate text, confidence scores,
    and bounding box coordinates.

    Args:
        file: Uploaded image file (JPEG, PNG, or WebP format).

    Returns:
        DetectionResponse: List of detected license plates.

    Raises:
        HTTPException: 400 if file is empty, invalid, or too large.

    Example:
        ```bash
        curl -X POST http://localhost:8100/detect/ \\
            -F "file=@car_image.jpg"
        ```
    """
    # Check for empty file
    if not file.filename:
        logger.warning("Detection request with no filename")
        raise HTTPException(status_code=400, detail="No filename provided")

    # Read file content
    content = await file.read()

    if len(content) == 0:
        logger.warning("Detection request with empty file")
        raise HTTPException(status_code=400, detail="Empty file uploaded")

    logger.info(
        "Processing detection request",
        extra={
            "filename": file.filename,
            "content_type": file.content_type,
            "size": len(content),
        },
    )

    try:
        # Call the detection service
        response = detect_plates(content)
        return response
    except FileTooLargeError as e:
        logger.warning(
            "File too large",
            extra={
                "size": e.size,
                "max_size": e.max_size,
            },
        )
        raise HTTPException(status_code=400, detail=str(e))
    except InvalidImageError as e:
        logger.warning(
            "Invalid image",
            extra={"error": str(e)},
        )
        raise HTTPException(status_code=400, detail=str(e))
    except DetectionError as e:
        logger.error(
            "Detection error",
            extra={"error": str(e)},
        )
        raise HTTPException(status_code=500, detail=f"Detection failed: {e}")