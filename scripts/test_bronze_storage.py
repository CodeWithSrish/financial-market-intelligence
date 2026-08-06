from app.services.coingecko_service import CoinGeckoService
from app.storage.bronze_storage import BronzeStorage


def main() -> None:
    """
    Test Bronze layer storage.
    """

    service = CoinGeckoService()

    storage = BronzeStorage()

    markets = service.get_top_markets()

    file_path = storage.save_json(
        source="coingecko",
        filename_prefix="markets",
        data=markets,
    )

    print(f"Saved file: {file_path}")

    service.close()


if __name__ == "__main__":
    main()