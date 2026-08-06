import json

from app.storage.bronze_storage import BronzeStorage
from app.validation.coin_market_validator import CoinMarketValidator


def main() -> None:
    """
    Validate Bronze data.
    """

    bronze_path = (
        "data/bronze/coingecko"
    )

    latest_file = sorted(
        BronzeStorage().base_directory.glob(
            "coingecko/*/*/*/*.json"
        )
    )[-1]

    with open(
        latest_file,
        encoding="utf-8",
    ) as file:
        raw_data = json.load(file)

    validated = CoinMarketValidator.validate(
        raw_data
    )

    print(
        f"Validated {len(validated)} records."
    )

    print(validated[0])


if __name__ == "__main__":
    main()