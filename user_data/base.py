from abc import ABC, abstractmethod


class DataSaver(ABC):
    @abstractmethod
    def save(self, data):
        pass