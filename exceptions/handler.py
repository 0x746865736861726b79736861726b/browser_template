import os
import datetime

from loguru import logger


class ExceptionHandler:
    def __init__(self, page):
        self.page = page

    async def handle(self, exception):
        error_message = f"An error occurred: {str(exception)}"
        logger.error(error_message)

        if self.page:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            screenshot_path = os.path.join("screenshots", f"error_{timestamp}.png")
            await self.page.screenshot(path=screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")
