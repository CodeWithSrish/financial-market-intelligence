import json
from pathlib import Path

from app.transformation.silver_transformer import SilverTransformer


def main() -> None:
    """
    Test the Silver transformation layer.
    """

    bronze_files = sorted(
        Path("data/bronze").glob("coingecko/*/*/*/*.json")
    )

    latest_file = bronze_files[-1]

    with latest_file.open(
        encoding="utf-8",
    ) as file:
        raw_data = json.load(file)

    silver_data = SilverTransformer.transform(raw_data)

    print(f"Loaded {len(silver_data)} records")

    print()

    print(silver_data[0])


if __name__ == "__main__":
    main()