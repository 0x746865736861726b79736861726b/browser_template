from pydantic_settings import BaseSettings


class BrowserRedis(BaseSettings):
    HOST: str
    PORT: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


redis_settings = BrowserRedis()
