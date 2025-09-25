from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    SECRET_KEY: str = "sua-chave-secreta-padrao-altere-isso"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: Optional[str] = "sqlite:///./barbearia.db"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    OPENING_TIME: str = "08:00"
    CLOSING_TIME: str = "20:00"
    APPOINTMENT_DURATION: int = 30
    SMTP_SERVER: Optional[str] = None
    SMTP_PORT: Optional[int] = None
    EMAIL_USER: Optional[str] = None
    EMAIL_PASSWORD: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()