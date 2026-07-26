from app.clients.coingecko import CoinGeckoClient


def main() -> None:
    """
    Test the CoinGecko client.
    """

    client = CoinGeckoClient()

    print(client.ping())

    markets = client.get_markets()

    print(markets[0]["name"])
    print(markets[0]["current_price"])

    trending = client.get_trending()

    print(trending["coins"][0]["item"]["name"])

    client.close()


if __name__ == "__main__":
    main()