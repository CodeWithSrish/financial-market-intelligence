

from app.clients.coingecko import CoinGeckoClient


class CoinGeckoService:
    """
    Business service for CoinGecko.
    """

    def __init__(self) -> None:
        self.client = CoinGeckoClient()

    def get_top_markets(
        self,
        vs_currency: str = "usd",
        per_page: int = 100,
        page: int = 1,
    ) -> list[dict]:
        """
        Fetch raw market data.
        """

        return self.client.get_markets(
            vs_currency=vs_currency,
            per_page=per_page,
            page=page,
        )

    def get_trending(self) -> dict:
        """
        Fetch raw trending data.
        """

        return self.client.get_trending()

    def close(self) -> None:
        self.client.close()