import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Basic configuration
    APP_NAME: str = "o1-mini-AI-engine"
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", False)
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///project.db")

    # Redis
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
    
    # Authentication and Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")
    JWT_ALGORITHM: str = "HS256"

settings = Settings()
