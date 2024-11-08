from patchright.async_api import Page

from browser.pages.base_page import BasePage


class GooglePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
