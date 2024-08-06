from animal import Animal, abstractmethod

class Human(Animal):
    def __init__(self, firstname, lastname, food, drink) -> None:
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.food = food
        self.h_drink = drink

    def greet(self):
        return f"Hello,my name is {self.firstname} {self.lastname}"
    
    def eat(self):
        return f"I am eating "+self.food
    
    def drink(self):
        return f"I am drinking {self.h_drink}"
    
    def sleep(self):
        return f"I am sleeping..."