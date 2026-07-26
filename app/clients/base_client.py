"""
Reusable HTTP client for external API communication.
"""

from __future__ import annotations

from typing import Any

import httpx

from app.config.settings import settings
from app.exceptions import (
    APIAuthenticationError,
    APIConnectionError,
    APIRateLimitError,
    APITimeoutError,
)
from app.logging.logger import get_logger


class BaseHTTPClient:
    """
    Base HTTP client for communicating with external APIs.

    This class centralizes:
    - HTTP session management
    - Timeout configuration
    - Logging
    - Response validation
    - Exception handling
    """

    def __init__(
        self,
        base_url: str,
        timeout: float | None = None,
    ) -> None:
        """
        Initialize the HTTP client.

        Args:
            base_url:
                Base URL of the external API.

            timeout:
                Request timeout in seconds.
                If None, the configured default is used.
        """

        if timeout is None:
            timeout = settings.http_client_timeout

        self.base_url = base_url
        self.timeout = timeout

        self.logger = get_logger(
            f"HTTPClient:{self.base_url}"
        )

        self.client = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
        )

        self.logger.info(
            "Initialized HTTP client for %s",
            self.base_url,
        )

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any] | list[Any]:
        """
        Send an HTTP GET request.

        Args:
            endpoint:
                API endpoint.

            params:
                Optional query parameters.

        Returns:
            Parsed JSON response.

        Raises:
            APITimeoutError:
                If the request times out.

            APIConnectionError:
                If the connection fails.

            APIAuthenticationError:
                If authentication fails.

            APIRateLimitError:
                If the API rate limit is exceeded.
        """

        self.logger.info(
            "Sending GET request to %s",
            endpoint,
        )

        try:
            response = self.client.get(
                endpoint,
                params=params,
            )

        except httpx.TimeoutException as error:
            self.logger.error(
                "Request timed out: %s",
                endpoint,
            )
            raise APITimeoutError(
                f"Request timed out: {endpoint}"
            ) from error

        except httpx.ConnectError as error:
            self.logger.error(
                "Connection failed: %s",
                endpoint,
            )
            raise APIConnectionError(
                f"Unable to connect to {endpoint}"
            ) from error

        return self._handle_response(response)

    def _handle_response(
        self,
        response: httpx.Response,
    ) -> dict[str, Any] | list[Any]:
        """
        Validate an HTTP response.

        Args:
            response:
                HTTP response object.

        Returns:
            Parsed JSON payload.
        """

        self.logger.info(
            "Received HTTP %s",
            response.status_code,
        )

        if response.is_success:
            return response.json()

        if response.status_code == 401:
            raise APIAuthenticationError(
                "Authentication failed."
            )

        if response.status_code == 429:
            raise APIRateLimitError(
                "API rate limit exceeded."
            )

        raise APIConnectionError(
            f"Unexpected HTTP status code: {response.status_code}"
        )

    def close(self) -> None:
        """
        Close the HTTP client.
        """

        self.client.close()

        self.logger.info(
            "Closed HTTP client for %s",
            self.base_url,
        )