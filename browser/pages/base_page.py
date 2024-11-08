from patchright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def click_element(self, selector: str):
        await self.page.click(selector)

    async def enter_text(self, selector: str, text: str):
        await self.page.fill(selector, text)

    async def navigate_to_url(self, url: str):
        await self.page.goto(url)

    async def get_text(self, selector: str):
        return await self.page.inner_text(selector)

    async def take_screenshot(self, path: str):
        await self.page.screenshot(path=path)

    async def wait_for_element(self, selector: str):
        await self.page.wait_for_selector(selector)
