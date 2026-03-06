"""
Models package for Pydantic request/response schemas.

Exports:
    PlateDetection: Single license plate detection result.
    DetectionResponse: Response model for detection endpoint.
    DetectionRequest: Request model for detection parameters.
"""

from models.schemas import DetectionRequest, DetectionResponse, PlateDetection

__all__ = [
    "PlateDetection",
    "DetectionResponse",
    "DetectionRequest",
]