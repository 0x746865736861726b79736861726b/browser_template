from pydantic_settings import BaseSettings


class BrowserSettings(BaseSettings):
    BROWSER: str
    PLAYWRIGHT_HEADLESS: bool
    PLAYWRIGHT_SLOW_MO: int
    START_URL: str

    class Config:
        extra = "allow"
        env_file = ".env"
        env_file_encoding = "utf-8"


browser_settings = BrowserSettings()
