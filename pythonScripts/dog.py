from animal import Animal

class Dog(Animal):
    def __init__(self, food, drink) -> None:
        super().__init__()
        self.food = food
        self.d_drink = drink

    def greet(self):
        return "WooWooooo..."
    
    def eat(self):
        return self.food
    
    def sleep(self):
        return "sleeping dog"
    
    def drink(self):
        return self.d_drink