from typing import List

from browser.provider import PlaywrightBrowser
from browser.interfaces.abstract import BrowserInterface


class BrowserFacade:
    def __init__(self, browser_type: str = "playwright", extensions: List[str] = None):
        self._provider = self._get_provider(browser_type, extensions)

    def _get_provider(
        self, browser_type: str, extensions: List[str]
    ) -> BrowserInterface:
        if browser_type == "playwright":
            return PlaywrightBrowser(extensions=extensions)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

    async def start_browser(self):
        await self._provider.start_browser()

    async def open_page(self, url: str):
        page = await self._provider.get_page()
        await page.goto(url)

    async def close_browser(self):
        await self._provider.stop_browser()

    async def take_screenshot(self, path: str):
        try:
            page = await self._provider.get_page()
            await page.screenshot(path=path)
        except Exception as e:
            print(f"Error taking screenshot: {e}")
