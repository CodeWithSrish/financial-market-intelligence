from app.exceptions import APITimeoutError


def fetch_data() -> None:
    raise APITimeoutError("CoinGecko request timed out.")


try:
    fetch_data()

except APITimeoutError as error:
    print(f"Caught timeout error: {error}")