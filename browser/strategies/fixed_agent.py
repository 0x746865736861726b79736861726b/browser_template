from browser.interfaces.user_agent import UserAgentStrategy


class FixedUserAgent(UserAgentStrategy):
    def __init__(self, user_agent: str):
        self._user_agent = user_agent

    def get_user_agent(self) -> str:
        return self._user_agent
