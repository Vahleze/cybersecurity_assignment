from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def greet(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def drink(self):
        pass

    @abstractmethod
    def sleep(self):
        pass