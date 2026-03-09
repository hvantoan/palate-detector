"""
Tests for detection API endpoints.

Tests the license plate detection endpoint for proper handling
of file uploads, validation, and response structure.
"""

import pytest
from httpx import AsyncClient


class TestDetectionEndpoint:
    """Tests for the detection endpoint POST /detect/."""

    @pytest.mark.asyncio
    async def test_detect_valid_image_returns_ok(
        self, async_client: AsyncClient, sample_jpeg_bytes: bytes
    ) -> None:
        """Valid image should return 200 with detection results."""
        files = {"file": ("test.jpg", sample_jpeg_bytes, "image/jpeg")}
        response = await async_client.post("/detect/", files=files)

        assert response.status_code == 200
        data = response.json()
        assert "plates" in data
        assert isinstance(data["plates"], list)

    @pytest.mark.asyncio
    async def test_detect_valid_image_returns_expected_plate(
        self,
        async_client: AsyncClient,
        sample_jpeg_bytes: bytes,
        expected_detection_response: dict,
    ) -> None:
        """Valid image should return mock detection result."""
        files = {"file": ("test.jpg", sample_jpeg_bytes, "image/jpeg")}
        response = await async_client.post("/detect/", files=files)

        assert response.status_code == 200
        assert response.json() == expected_detection_response

    @pytest.mark.asyncio
    async def test_detect_valid_png_image(
        self, async_client: AsyncClient, sample_png_bytes: bytes
    ) -> None:
        """Valid PNG image should be processed correctly."""
        files = {"file": ("test.png", sample_png_bytes, "image/png")}
        response = await async_client.post("/detect/", files=files)

        assert response.status_code == 200
        data = response.json()
        assert "plates" in data

    @pytest.mark.asyncio
    async def test_detect_empty_file_returns_400(
        self, async_client: AsyncClient, empty_file_bytes: bytes
    ) -> None:
        """Empty file should return 400 error."""
        files = {"file": ("empty.jpg", empty_file_bytes, "image/jpeg")}
        response = await async_client.post("/detect/", files=files)

        assert response.status_code == 400
        assert "Empty file uploaded" in response.json()["detail"]

    @pytest.mark.asyncio
    async def test_detect_file_too_large_returns_400(
        self, async_client: AsyncClient, large_file_bytes: bytes
    ) -> None:
        """File exceeding size limit should return 400 error."""
        files = {"file": ("large.jpg", large_file_bytes, "image/jpeg")}
        response = await async_client.post("/detect/", files=files)

        assert response.status_code == 400
        detail = response.json()["detail"]
        assert "exceeds maximum allowed" in detail

    @pytest.mark.asyncio
    async def test_detect_small_invalid_image_returns_400(
        self, async_client: AsyncClient, small_invalid_bytes: bytes
    ) -> None:
        """Image data too small should return 400 error."""
        files = {"file": ("small.jpg", small_invalid_bytes, "image/jpeg")}
        response = await async_client.post("/detect/", files=files)

        assert response.status_code == 400
        detail = response.json()["detail"]
        assert "too small to be valid" in detail

    @pytest.mark.asyncio
    async def test_detection_response_has_plate_structure(
        self, async_client: AsyncClient, sample_jpeg_bytes: bytes
    ) -> None:
        """Detection response should contain properly structured plates."""
        files = {"file": ("test.jpg", sample_jpeg_bytes, "image/jpeg")}
        response = await async_client.post("/detect/", files=files)

        assert response.status_code == 200
        data = response.json()

        # Check response structure
        assert "plates" in data
        plates = data["plates"]
        assert isinstance(plates, list)

        # If plates found, check structure
        if plates:
            plate = plates[0]
            assert "plate_text" in plate
            assert "confidence" in plate
            assert "bbox" in plate
            assert isinstance(plate["confidence"], (int, float))
            assert isinstance(plate["bbox"], list)
            assert len(plate["bbox"]) == 4