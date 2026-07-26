"""
Reusable HTTP client for external API communication.
"""

from __future__ import annotations

import httpx

from app.config.settings import settings
from app.logging.logger import get_logger


class BaseHTTPClient:
    """
    Base HTTP client for communicating with external APIs.

    This class provides a reusable HTTP session,
    timeout configuration, and centralized logging.
    """

    def __init__(
        self,
        base_url: str,
    ) -> None:
        """
        Initialize the HTTP client.

        Args:
            base_url:
                Base URL for the API.
        """

        self.logger = get_logger(self.__class__.__name__)

        self.base_url = base_url

        self.timeout = httpx.Timeout(
            connect=10.0,
            read=30.0,
            write=30.0,
            pool=30.0,
        )

        self.client = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
        )

        self.logger.info(
            "Initialized HTTP client for %s",
            self.base_url,
        )

    def close(self) -> None:
        """
        Close the HTTP session.
        """

        self.client.close()

        self.logger.info(
            "Closed HTTP client for %s",
            self.base_url,
        )