from typing import List

from fake_useragent import UserAgent
from playwright.async_api import async_playwright

from browser.interfaces.abstract import BrowserInterface


class PlaywrightBrowser(BrowserInterface):
    def __init__(self, extensions: List[str] = None):
        # super().__init__()
        self._playwright = None
        self._browser = None
        self._context = None
        self._user_agent = UserAgent()
        self._extensions = extensions if extensions else []

    async def start_browser(self):
        random_user_agent = self._user_agent.random
        extensions_arg = ""
        if self._extensions:
            extensions_arg = "--load-extension={','.join(self._extensions)}"

        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-web-security",
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--disable-extensions",
                "--disable-software-rasterizer",
                "--lang=en-US",
                extensions_arg,
            ],
        )
        self._context = await self._browser.new_context(
            user_agent=random_user_agent,
            viewport={"width": 1920, "height": 1080},
            locale="en-US",
        )
        self._page = await self._context.new_page()
        await self._page.evaluate(
            """
            () => {
                Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
                window.chrome = { runtime: {} }; 
                Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
                Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
            }
            """
        )

    async def get_page(self):
        if not self._page:
            raise RuntimeError("Browser page is not initialized.")
        return self._page

    async def stop_browser(self):
        if self._context:
            await self._context.close()
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
