from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    """Sample abstract class of ABC"""

    @abstractmethod
    def run(self) -> int:
        pass

    @abstractmethod
    def sleep(self) -> int:
        pass
