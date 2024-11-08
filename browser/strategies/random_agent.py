from fake_useragent import UserAgent

from browser.interfaces.user_agent import UserAgentStrategy


class RandomUserAgent(UserAgentStrategy):
    def __init__(self):
        self._user_agent = UserAgent()

    def get_user_agent(self) -> str:
        return self._user_agent.random
