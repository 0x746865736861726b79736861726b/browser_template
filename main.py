import asyncio

from browser.facade import BrowserFacade
from browser.pages.gmail import GmailPage
from exceptions.handler import ExceptionHandler
from user_data.generators import UserDataGenerator
from user_data.saver import CSVSaver
from user_data.service import UserDataService


async def main():
    # extesions_path = [
    #     "extensions/WebRTC-Leak-Shield-Chrome.crx",
    # ]
    try:
        browser_facade = BrowserFacade(browser_type="playwright")
        await browser_facade.start_browser()
        page = await browser_facade._provider.get_page()
        page_actions = GmailPage(page)
        await page_actions.open_page("https://gmail.com/")
        await page_actions.signup()
        # await browser_facade.open_page("https://bot.sannysoft.com")
        await asyncio.sleep(20)
    except Exception as e:
        # Створення обробника помилок
        exception_handler = ExceptionHandler(page)
        await exception_handler.handle(e)

    finally:
        # Закриття браузера після всіх дій
        await browser_facade.close_browser()


asyncio.run(main())
