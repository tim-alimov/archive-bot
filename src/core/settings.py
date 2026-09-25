from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr = Field(...)
    admin_id: int = Field(...)
    archive_channel_id: int = Field(...)

    database_url: SecretStr = Field(...)

    debug: bool = Field(...)
    log_level: str = Field(...)

    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        case_sensitive=False,
        env_file_encoding="utf-8",
    )


settings = Settings()  # pyright: ignore[reportCallIssue]
