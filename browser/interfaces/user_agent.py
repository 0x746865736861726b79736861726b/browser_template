from abc import ABC, abstractmethod


class UserAgentStrategy(ABC):
    @abstractmethod
    def get_user_agent(self) -> str:
        pass
