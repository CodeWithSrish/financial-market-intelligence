from app.clients.base_client import BaseHTTPClient


def main() -> None:
    """
    Test the BaseHTTPClient.
    """

    client = BaseHTTPClient(
        base_url="https://api.coingecko.com/api/v3",
    )

    client.close()


if __name__ == "__main__":
    main()