"""
Uvicorn server startup script for the AI Service.

Runs the FastAPI application using uvicorn with configurable settings.
Settings can be overridden via environment variables (PORT, HOST, RELOAD).

Usage:
    python run.py
    PORT=9000 python run.py
    HOST=127.0.0.1 PORT=8200 RELOAD=true python run.py
"""

import logging
import sys

import uvicorn

from config import get_settings


def setup_logging(log_level: str) -> None:
    """
    Configure logging for the application.

    Args:
        log_level: Logging level string (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def main() -> None:
    """
    Main entry point to start the uvicorn server.

    Reads configuration from Settings (supports environment variables).
    Starts uvicorn with the configured host, port, and reload settings.
    """
    settings = get_settings()

    # Configure logging
    setup_logging(settings.log_level)

    logger = logging.getLogger(__name__)
    logger.info(
        f"Starting AI Service on {settings.host}:{settings.port} "
        f"(reload={'enabled' if settings.reload else 'disabled'})"
    )

    # Run uvicorn server
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )


if __name__ == "__main__":
    main()