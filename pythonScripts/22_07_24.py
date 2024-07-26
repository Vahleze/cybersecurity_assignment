from user import User

class Person:
    def  __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    def __str__(self):
        return f"{self.name} {self.phonenumber}"
    
    def getName(self):
        return f"Hello, my name  is {self.name}"



person1 = Person("Chidubem", "08160501384")
print(person1.name) 
print(person1.phonenumber)
print(person1) 
print(person1.getName())

Esther = Person("Esther", "0831834672")
print(Esther.name)
print(Esther.phonenumber)
print(Esther)
print(Esther.getName())


user1 = User("Mathias", "Oba", "mathyhart@gmail.com", "mathy01010")
print(user1)
print(user1.greet())
print(user1.getLoginDetails())
print(user1.created_at) 