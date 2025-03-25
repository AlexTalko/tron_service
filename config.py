from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./tron_service.db"
    TRON_NETWORK: str = "shasta"  # or "mainnet"

    class Config:
        env_file = ".env"


settings = Settings()
