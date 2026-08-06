from __future__ import annotations

from app.models.coin_market import CoinMarket
from app.validation.coin_market_validator import CoinMarketValidator


class SilverTransformer:
    """
    Transforms Bronze data into Silver objects.
    """

    @staticmethod
    def transform(records: list[dict]) -> list[CoinMarket]:
        """
        Transform Bronze records into Silver objects.
        """
        validated_records = CoinMarketValidator.validate(records)

        return sorted(
            validated_records,
            key=lambda coin: coin.market_cap_rank,
        )