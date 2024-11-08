import random

from browser.interfaces.user_agent import UserAgentStrategy


class ListUserAgent(UserAgentStrategy):
    def __init__(self, user_agents: list):
        self._user_agents = user_agents

    def get_user_agent(self) -> str:
        return random.choice(self._user_agents)
