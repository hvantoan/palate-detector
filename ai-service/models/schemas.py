"""
Pydantic models for request/response schemas.

Defines data models for license plate detection API.
"""

from typing import List

from pydantic import BaseModel, Field


class PlateDetection(BaseModel):
    """
    Single license plate detection result.

    Attributes:
        plate_text: The recognized text from the license plate.
        confidence: Detection confidence score (0.0 to 1.0).
        bbox: Bounding box coordinates [x1, y1, x2, y2].
    """

    plate_text: str = Field(
        ...,
        description="The recognized text from the license plate",
        examples=["51F-123.45"],
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Detection confidence score (0.0 to 1.0)",
        examples=[0.95],
    )
    bbox: List[int] = Field(
        ...,
        min_length=4,
        max_length=4,
        description="Bounding box coordinates [x1, y1, x2, y2]",
        examples=[[100, 100, 300, 150]],
    )


class DetectionResponse(BaseModel):
    """
    Response model for plate detection endpoint.

    Attributes:
        plates: List of detected license plates.
    """

    plates: List[PlateDetection] = Field(
        default_factory=list,
        description="List of detected license plates",
    )


class DetectionRequest(BaseModel):
    """
    Request model for detection endpoint metadata.

    Note: Actual image data is sent via multipart/form-data,
    but this model can be used for additional request parameters.
    """

    confidence_threshold: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Override default confidence threshold for this request",
    )