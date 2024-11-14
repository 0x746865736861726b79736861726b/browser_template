from patchright.async_api import Page

from browser.pages.base_page import BasePage


class GmailPage(BasePage):
    CREATE_ACCOUT_BUTTON = "//button[span[text()='Create account']]"
    PERSONAL_USE_OPTION = "//span[text()='For my personal use']"

    async def open_page(self, url: str):
        await self.navigate_to_url(url)

    async def signup(self):
        await self.click_element(self.CREATE_ACCOUT_BUTTON)
        await self.wait_for_element(self.PERSONAL_USE_OPTION)
        await self.click_element(self.PERSONAL_USE_OPTION)
