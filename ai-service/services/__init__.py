"""
Services package for business logic.

Exports:
    detect_plates: License plate detection function.
"""

from services.detection import detect_plates

__all__ = [
    "detect_plates",
]