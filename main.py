import asyncio
from browser.facade import BrowserFacade


async def main():
    extesions_path = [
        "extensions/WebRTC-Leak-Shield-Chrome.crx",
    ]
    browser_facade = BrowserFacade(browser_type="playwright", extensions=extesions_path)
    await browser_facade.start_browser()
    await browser_facade.open_page("https://www.browserscan.net/")
    await asyncio.sleep(20)
    await browser_facade.take_screenshot("screenshots/screenshot.png")

    await browser_facade.close_browser()


asyncio.run(main())
