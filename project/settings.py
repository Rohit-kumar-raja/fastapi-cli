from pathlib import Path
from dotenv import load_dotenv
from pydantic import Field, AnyUrl
from pydantic_settings import BaseSettings


# Define the base path directly
BASE_DIR = Path(__file__).resolve().parent.parent
class Settings(BaseSettings):
    BASE_DIR: Path = BASE_DIR

    # Application settings
    APP_ENV: str = Field(..., description="Environment mode (development/production)")
    APP_HOST: str = Field(..., description="Application host")
    APP_PORT: int = Field(..., description="Application port")
    APP_SECRET_KEY: str = Field(..., description="Secret key for the application")
    APP_ALLOWED_ORIGIN: str = Field(..., description="Comma-separated allowed origins")
    APP_CONTAINER: str = Field(..., description="Container name")
    APP_NETWORK: str = Field(..., description="Network name")
    APP_LOG_PATH: Path = Field(..., description="Path to application log file")
    APP_LOG_LEVEL: str = Field(..., description="Log level for the application")

    # Database settings
    DB_HOST: str = Field(..., description="Database host")
    DB_PORT: int = Field(..., description="Database port")
    DB_NAME: str = Field(..., description="Database name")
    DB_USER: str = Field(..., description="Database user")
    DB_PASSWORD: str = Field(..., description="Database password")
    DB_CONTAINER: str = Field(..., description="Database container name")
    DB_VOLUME: str = Field(..., description="Database volume")

    # Email settings
    SMTP_SERVER: str = Field(..., description="SMTP server")
    SMTP_PORT: int = Field(..., description="SMTP port")
    SENDER_EMAIL: str = Field(..., description="Sender email")
    SMTP_USERNAME: str = Field(..., description="Smtp server username")
    SMTP_PASSWORD: str = Field(..., description="SMTP password")

    # PGAdmin settings
    PGADMIN_DEFAULT_EMAIL: str = Field(..., description="PGAdmin default email")
    PGADMIN_DEFAULT_PASSWORD: str = Field(..., description="PGAdmin default password")
    PGADMIN_SERVER_PORT: int = Field(..., description="PGAdmin server port")
    PGADMIN_CONTAINER: str = Field(..., description="PGAdmin container")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# settings = Settings()

def reload_settings() -> Settings:
    load_dotenv(override=True)  # Reload .env values, override any existing env vars
    return Settings()  # Return the new instance of Settings
settings=reload_settings()