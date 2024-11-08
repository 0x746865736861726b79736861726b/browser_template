import asyncio
from browser.facade import BrowserFacade
from browser.pages.google import GooglePage


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
    await browser_facade.open_page("https://www.browserscan.net/")
    await asyncio.sleep(20)
    await browser_facade.take_screenshot("screenshots/screenshot.png")

    await browser_facade.close_browser()


asyncio.run(main())
