from app.clients.coingecko import CoinGeckoClient
from app.models.coin_market import CoinMarket


def main() -> None:
    """
    Validate CoinGecko market data using Pydantic.
    """

    client = CoinGeckoClient()

    markets = client.get_markets()

    coin = CoinMarket.model_validate(markets[0])

    print(coin)

    print()

    print(coin.name)

    print(coin.current_price)

    client.close()


if __name__ == "__main__":
    main()