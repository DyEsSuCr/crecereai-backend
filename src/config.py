from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TITLE_API: str
    DESCRIPTION_API: str

    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str

    JWT_SECRET: str
    JWT_ALGORITHM: str
    REFRESH_TOKEN_EXPIRY: int = 2
    ACCESS_TOKEN_EXPIRY: int = 3600

    REDIS_URL: str = "redis://localhost:6379/0"

    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False

    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    DOMAIN: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()


broker_url = Config.REDIS_URL
result_backend = Config.REDIS_URL
broker_connection_retry_on_startup = True
