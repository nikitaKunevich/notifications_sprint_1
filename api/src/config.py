from pydantic import BaseSettings


class Settings(BaseSettings):
    log_level: str = "INFO"

    rabbit_events_queue_name: str
    rabbit_username: str
    rabbit_password: str
    rabbit_host: str
    rabbit_exchange: str
    rabbit_exchange_type: str


settings = Settings()
