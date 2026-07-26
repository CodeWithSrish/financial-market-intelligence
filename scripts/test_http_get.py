from app.clients.base_client import BaseHTTPClient


def main() -> None:
    client = BaseHTTPClient(
        base_url="https://api.coingecko.com/api/v3",
    )

    data = client.get("/ping")

    print(data)

    client.close()


if __name__ == "__main__":
    main()