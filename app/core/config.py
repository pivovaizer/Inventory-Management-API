from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    """Application settings."""
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "Inventory Management API"
    debug: bool = True
    database_url: str = "sqlite:///./inventory.db"
    secret_key: str = "your_secret_key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
settings = Settings()
    
