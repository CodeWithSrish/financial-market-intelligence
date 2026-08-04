"""
Pydantic model representing a cryptocurrency market record.
"""

from pydantic import BaseModel


class CoinMarket(BaseModel):
    """
    Represents a cryptocurrency returned by the CoinGecko Markets API.
    """

    id: str
    symbol: str
    name: str

    current_price: float

    market_cap: float

    market_cap_rank: int

    total_volume: float

    price_change_percentage_24h: float | None = None

    last_updated: str