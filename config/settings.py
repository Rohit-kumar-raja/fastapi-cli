# Settings Configuration# Database Configuration
from pydantic import Field
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

""" The purpose for this file to for getting the data from .env file   """

class AppSettings(BaseSettings):
     # FastAPI application settings
    app_name: str = Field("FastAPIApp", env="APP_NAME")
    app_env: str = Field("local", env="APP_ENV")
    app_debug: bool = Field(True, env="APP_DEBUG")
    app_url: str = Field("http://localhost", env="APP_URL")
    
    # Logging settings
    log_channel: str = Field("stack", env="LOG_CHANNEL")
    log_level: str = Field("debug", env="LOG_LEVEL")
    
    # PostgreSQL Configuration
    db_connection: Optional[str] = Field(None, env="DB_CONNECTION")
    db_host: str = Field("127.0.0.1", env="DB_HOST")
    db_port: int = Field(5432, env="DB_PORT")
    db_database: str = Field("forge", env="DB_DATABASE")
    db_username: str = Field("forge", env="DB_USERNAME")
    db_password: str = Field("", env="DB_PASSWORD")
    pgsql_charset: str = "utf8"
    pgsql_sslmode: str = Field("prefer", env="DB_SSLMODE")   
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Load settings

def reload_settings() -> AppSettings:
    load_dotenv(override=True)  # Reload .env values, override any existing env vars
    return AppSettings()  # Return the new instance of Settings
settings=reload_settings()
