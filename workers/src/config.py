from pydantic import BaseSettings


class Settings(BaseSettings):
    sleep_time: int = 10
    log_level: str = "INFO"
    default_timeout_for_requests: int = 2

    rabbit_email_exchange: str
    rabbit_email_exchange_type: str
    rabbit_email_queues: list[str]
    rabbit_email_routing_key: str
    rabbit_username: str
    rabbit_password: str
    rabbit_host: str

    postgres_db: str = "postgres"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"

    url_auth_service: str

    @property
    def database_settings(self) -> dict:
        return {
            "dbname": self.postgres_db,
            "user": self.postgres_user,
            "password": self.postgres_password,
            "host": self.postgres_host,
            "port": self.postgres_port,
        }

    @property
    def database_uri(self):
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


settings = Settings()