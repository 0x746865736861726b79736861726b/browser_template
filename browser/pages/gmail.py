from patchright.async_api import Page

from browser.pages.base_page import BasePage


class GmailPage(BasePage):

    async def open_page(self, url: str):
        await self.page.goto(url)

    async def signup(self):
        await self.page.locator("//button[span[text()='Create account']]").click()
        await self.page.wait_for_load_state("networkidle")
        await self.page.locator("//span[text()='For my personal use']").click()
