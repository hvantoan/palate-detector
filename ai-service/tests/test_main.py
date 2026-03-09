"""
Tests for main.py FastAPI application endpoints.

Tests the root and health check endpoints for proper response structure
and status codes.
"""

import pytest
from httpx import AsyncClient


class TestRootEndpoint:
    """Tests for the root endpoint GET /."""

    @pytest.mark.asyncio
    async def test_root_returns_ok_status(self, async_client: AsyncClient) -> None:
        """Root endpoint should return status 'ok'."""
        response = await async_client.get("/")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"

    @pytest.mark.asyncio
    async def test_root_returns_service_name(
        self, async_client: AsyncClient
    ) -> None:
        """Root endpoint should return the service name."""
        response = await async_client.get("/")

        assert response.status_code == 200
        data = response.json()
        assert data["service"] == "palate-detector-ai"

    @pytest.mark.asyncio
    async def test_root_response_structure(
        self, async_client: AsyncClient, expected_root_response: dict
    ) -> None:
        """Root endpoint should return expected response structure."""
        response = await async_client.get("/")

        assert response.status_code == 200
        assert response.json() == expected_root_response


class TestHealthEndpoint:
    """Tests for the health check endpoint GET /health."""

    @pytest.mark.asyncio
    async def test_health_returns_ok_status(
        self, async_client: AsyncClient
    ) -> None:
        """Health endpoint should return status 'ok'."""
        response = await async_client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"

    @pytest.mark.asyncio
    async def test_health_response_structure(
        self, async_client: AsyncClient, expected_health_response: dict
    ) -> None:
        """Health endpoint should return expected response structure."""
        response = await async_client.get("/health")

        assert response.status_code == 200
        assert response.json() == expected_health_response

    @pytest.mark.asyncio
    async def test_health_has_only_status_key(
        self, async_client: AsyncClient
    ) -> None:
        """Health endpoint response should only contain status key."""
        response = await async_client.get("/health")

        data = response.json()
        assert set(data.keys()) == {"status"}