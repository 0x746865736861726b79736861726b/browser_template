from abc import ABC, abstractmethod


class BrowserInterface(ABC):
    def __init__(self):
        self._page = None

    @abstractmethod
    async def start_browser(self):
        pass

    @abstractmethod
    async def get_page(self):
        pass

    @abstractmethod
    async def stop_browser(self):
        pass
