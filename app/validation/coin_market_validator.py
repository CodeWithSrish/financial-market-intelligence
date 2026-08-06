from __future__ import annotations

from app.models.coin_market import CoinMarket


class CoinMarketValidator:
    """
    Validates raw CoinGecko market records.
    """

    @staticmethod
    def validate(
        records: list[dict],
    ) -> list[CoinMarket]:
        """
        Validate raw JSON records and return
        strongly typed CoinMarket objects.
        """

        return [
            CoinMarket.model_validate(record)
            for record in records
        ]