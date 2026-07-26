from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    gcp_project_id: str
    gcp_region: str

    gcs_bronze_bucket: str

    coingecko_api_key: str = ""
    alpha_vantage_api_key: str = ""
    news_api_key: str = ""

    environment: str = "development"

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


@lru_cache    # lru means Least Recently Used Cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.
    """
    return Settings()


settings = get_settings()