import asyncio
from browser.facade import BrowserFacade
from browser.pages.gmail import GmailPage
from browser.pages.google import GooglePage
from browser.pages.instagram import InstagramPage


async def main():
    extesions_path = [
        "extensions/WebRTC-Leak-Shield-Chrome.crx",
    ]
    browser_facade = BrowserFacade(browser_type="playwright", extensions=extesions_path)
    await browser_facade.start_browser()
    # page = await browser_facade._provider.get_page()
    # page_actions = GooglePage(page)
    # await page_actions.navigate_to_url("https://www.google.com/")
    # await page_actions.get_screenshot()
    page = await browser_facade._provider.get_page()
    # page_actions = InstagramPage(page)
    # await page_actions.open_page("https://instagram.com/")
    # await page_actions.signup()

    page_actions = GmailPage(page)
    await page_actions.open_page("https://gmail.com/")
    await page_actions.signup()

    # await browser_facade.open_page("https://google.com/")
    # await browser_facade.open_page("https://instagram.com/")
    # await browser_facade.open_page("https://bot.sannysoft.com")
    await asyncio.sleep(20)
    await browser_facade.take_screenshot("screenshots/screenshot.png")

    await browser_facade.close_browser()


asyncio.run(main())
