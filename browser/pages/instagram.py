from patchright.async_api import Page
from browser.pages.base_page import BasePage


class InstagramPage(BasePage):
    async def open_page(self, url: str):
        await self.page.goto(url)

    async def signup(self):
        await self.click_element("//section/main/article//span/p/a")
        await self.page.wait_for_load_state("networkidle")
        await self.page.is_visible("//input[@name='emailOrPhone']")
        await self.page.click("//input[@name='emailOrPhone']")


# //section/main/article//span/p/a
