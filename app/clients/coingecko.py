"""
CoinGecko API client.
"""

from __future__ import annotations

from typing import Any

from app.clients.base_client import BaseHTTPClient


class CoinGeckoClient:
    """
    Client for interacting with the CoinGecko API.
    """

    BASE_URL = "https://api.coingecko.com/api/v3"

    PING_ENDPOINT = "/ping"
    MARKETS_ENDPOINT = "/coins/markets"
    TRENDING_ENDPOINT = "/search/trending"

    def __init__(self) -> None:
        """
        Initialize the CoinGecko client.
        """

        self.http_client = BaseHTTPClient(
            base_url=self.BASE_URL,
        )

    def ping(self) -> dict[str, Any]:
        """
        Check whether the CoinGecko API is reachable.

        Returns:
            API health response.
        """

        return self.http_client.get(
            self.PING_ENDPOINT,
        )

    def get_markets(
        self,
        vs_currency: str = "usd",
        per_page: int = 10,
        page: int = 1,
    ) -> list[dict[str, Any]]:
        """
        Retrieve cryptocurrency market data.

        Args:
            vs_currency:
                Currency for prices.

            per_page:
                Number of coins.

            page:
                Page number.

        Returns:
            List of market records.
        """

        response = self.http_client.get(
            self.MARKETS_ENDPOINT,
            params={
                "vs_currency": vs_currency,
                "per_page": per_page,
                "page": page,
            },
        )

        return response  # type: ignore[return-value]

    def get_trending(self) -> dict[str, Any]:
        """
        Retrieve trending cryptocurrencies.

        Returns:
            Trending coins.
        """

        response = self.http_client.get(
            self.TRENDING_ENDPOINT,
        )

        return response  # type: ignore[return-value]

    def close(self) -> None:
        """
        Close the underlying HTTP client.
        """

        self.http_client.close()