"""
Pytest configuration and fixtures for AI Service tests.

Provides shared fixtures for testing FastAPI endpoints and
detection service functionality.
"""

import io
from collections.abc import Generator
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

# Import the FastAPI app
# Note: imports are done inside fixtures to avoid issues with
# missing dependencies during test collection
from main import app


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """Configure anyio backend for async tests."""
    return "asyncio"


@pytest.fixture
def client() -> Generator[AsyncClient, None, None]:
    """
    Create a test client for the FastAPI application.

    Uses httpx.AsyncClient with ASGITransport for async endpoint testing.
    Yields the client for use in tests.

    Yields:
        AsyncClient: HTTP client configured for the test app.
    """
    transport = ASGITransport(app=app)
    with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest_asyncio.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """
    Create an async test client for the FastAPI application.

    Preferred for async endpoints that need async context.

    Yields:
        AsyncClient: HTTP client configured for the test app.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


# ============================================================================
# Sample Image Fixtures
# ============================================================================

@pytest.fixture
def sample_jpeg_bytes() -> bytes:
    """
    Create minimal valid JPEG bytes for testing.

    This is a 1x1 white pixel JPEG image - the smallest valid JPEG.
    Useful for testing file upload without needing actual image files.

    Returns:
        bytes: Minimal valid JPEG image data.
    """
    # Minimal valid JPEG: 1x1 white pixel
    # This is the smallest valid JPEG that most decoders accept
    return bytes([
        0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46,
        0x49, 0x46, 0x00, 0x01, 0x01, 0x00, 0x00, 0x01,
        0x00, 0x01, 0x00, 0x00, 0xFF, 0xDB, 0x00, 0x43,
        0x00, 0x08, 0x06, 0x06, 0x07, 0x06, 0x05, 0x08,
        0x07, 0x07, 0x07, 0x09, 0x09, 0x08, 0x0A, 0x0C,
        0x14, 0x0D, 0x0C, 0x0B, 0x0B, 0x0C, 0x19, 0x12,
        0x13, 0x0F, 0x14, 0x1D, 0x1A, 0x1F, 0x1E, 0x1D,
        0x1A, 0x1C, 0x1C, 0x20, 0x24, 0x2E, 0x27, 0x20,
        0x22, 0x2C, 0x23, 0x1C, 0x1C, 0x28, 0x37, 0x29,
        0x2C, 0x30, 0x31, 0x34, 0x34, 0x34, 0x1F, 0x27,
        0x39, 0x3D, 0x38, 0x32, 0x3C, 0x2E, 0x33, 0x34,
        0x32, 0xFF, 0xC0, 0x00, 0x0B, 0x08, 0x00, 0x01,
        0x00, 0x01, 0x01, 0x01, 0x11, 0x00, 0xFF, 0xC4,
        0x00, 0x1F, 0x00, 0x00, 0x01, 0x05, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x03, 0x04,
        0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0xFF,
        0xC4, 0x00, 0xB5, 0x10, 0x00, 0x02, 0x01, 0x03,
        0x03, 0x02, 0x04, 0x03, 0x05, 0x05, 0x04, 0x04,
        0x00, 0x00, 0x01, 0x7D, 0x01, 0x02, 0x03, 0x00,
        0x04, 0x11, 0x05, 0x12, 0x21, 0x31, 0x41, 0x06,
        0x13, 0x51, 0x61, 0x07, 0x22, 0x71, 0x14, 0x32,
        0x81, 0x91, 0xA1, 0x08, 0x23, 0x42, 0xB1, 0xC1,
        0x15, 0x52, 0xD1, 0xF0, 0x24, 0x33, 0x62, 0x72,
        0x82, 0x09, 0x0A, 0x16, 0x17, 0x18, 0x19, 0x1A,
        0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x34, 0x35,
        0x36, 0x37, 0x38, 0x39, 0x3A, 0x43, 0x44, 0x45,
        0x46, 0x47, 0x48, 0x49, 0x4A, 0x53, 0x54, 0x55,
        0x56, 0x57, 0x58, 0x59, 0x5A, 0x63, 0x64, 0x65,
        0x66, 0x67, 0x68, 0x69, 0x6A, 0x73, 0x74, 0x75,
        0x76, 0x77, 0x78, 0x79, 0x7A, 0x83, 0x84, 0x85,
        0x86, 0x87, 0x88, 0x89, 0x8A, 0x92, 0x93, 0x94,
        0x95, 0x96, 0x97, 0x98, 0x99, 0x9A, 0xA2, 0xA3,
        0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9, 0xAA, 0xB2,
        0xB3, 0xB4, 0xB5, 0xB6, 0xB7, 0xB8, 0xB9, 0xBA,
        0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9,
        0xCA, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7, 0xD8,
        0xD9, 0xDA, 0xE1, 0xE2, 0xE3, 0xE4, 0xE5, 0xE6,
        0xE7, 0xE8, 0xE9, 0xEA, 0xF1, 0xF2, 0xF3, 0xF4,
        0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFF, 0xDA,
        0x00, 0x08, 0x01, 0x01, 0x00, 0x00, 0x3F, 0x00,
        0xFB, 0xD5, 0xDB, 0x20, 0xB8, 0xE3, 0x9E, 0x76,
        0xEB, 0x1D, 0xFF, 0xD9,
    ])


@pytest.fixture
def sample_png_bytes() -> bytes:
    """
    Create minimal valid PNG bytes for testing.

    This is a 1x1 white pixel PNG image - the smallest valid PNG.
    Useful for testing different image format uploads.

    Returns:
        bytes: Minimal valid PNG image data.
    """
    # Minimal valid PNG: 1x1 white pixel
    return bytes([
        0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,  # PNG signature
        0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,  # IHDR chunk
        0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,
        0x08, 0x02, 0x00, 0x00, 0x00, 0x90, 0x77, 0x53,
        0xDE,
        0x00, 0x00, 0x00, 0x0C, 0x49, 0x44, 0x41, 0x54,  # IDAT chunk
        0x08, 0xD7, 0x63, 0xF8, 0xFF, 0xFF, 0xFF, 0x00,
        0x05, 0xFE, 0x02, 0xFE,
        0xDC, 0xCC, 0x59, 0xE7,
        0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44,  # IEND chunk
        0xAE, 0x42, 0x60, 0x82,
    ])


@pytest.fixture
def empty_file_bytes() -> bytes:
    """
    Create empty bytes for testing empty file upload handling.

    Returns:
        bytes: Empty bytes.
    """
    return b""


@pytest.fixture
def small_invalid_bytes() -> bytes:
    """
    Create small bytes that are too small to be a valid image.

    The detection service rejects images smaller than 100 bytes.

    Returns:
        bytes: Small invalid data (50 bytes).
    """
    return b"x" * 50


@pytest.fixture
def large_file_bytes() -> bytes:
    """
    Create bytes exceeding the maximum upload size limit.

    Default max_upload_size is 10MB (10,485,760 bytes).
    This creates 11MB of data to trigger FileTooLargeError.

    Returns:
        bytes: Data exceeding upload size limit (11MB).
    """
    return b"x" * (11 * 1024 * 1024)  # 11MB


# ============================================================================
# File-like Object Fixtures
# ============================================================================

@pytest.fixture
def sample_jpeg_file(sample_jpeg_bytes: bytes) -> io.BytesIO:
    """
    Create a file-like object containing JPEG data.

    Args:
        sample_jpeg_bytes: JPEG bytes fixture.

    Returns:
        io.BytesIO: File-like object with JPEG data.
    """
    return io.BytesIO(sample_jpeg_bytes)


@pytest.fixture
def empty_file() -> io.BytesIO:
    """
    Create an empty file-like object.

    Returns:
        io.BytesIO: Empty file-like object.
    """
    return io.BytesIO(b"")


# ============================================================================
# Test Data Fixtures
# ============================================================================

@pytest.fixture
def expected_detection_response() -> dict:
    """
    Expected response structure for successful detection.

    Returns:
        dict: Expected mock detection response.
    """
    return {
        "plates": [
            {
                "plate_text": "51F-123.45",
                "confidence": 0.95,
                "bbox": [100, 100, 300, 150],
            }
        ]
    }


@pytest.fixture
def expected_empty_response() -> dict:
    """
    Expected response structure when no plates are detected.

    Returns:
        dict: Empty plates response.
    """
    return {"plates": []}


@pytest.fixture
def expected_health_response() -> dict:
    """
    Expected response structure for health check endpoint.

    Returns:
        dict: Health check response.
    """
    return {"status": "ok"}


@pytest.fixture
def expected_root_response() -> dict:
    """
    Expected response structure for root endpoint.

    Returns:
        dict: Root endpoint response.
    """
    return {"status": "ok", "service": "palate-detector-ai"}