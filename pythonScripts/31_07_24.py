from triangle import Triangle
from square import Square
from animal import Animal
from human import Human
from dog import Dog

tri1 = Triangle(5, 4)
sqr1 = Square(6)

print(tri1.area())
print(tri1.perimeter())
print(sqr1.area())
print(sqr1.perimeter())

Helen = Human("HelenBuns", "Oluchukwu", "Rice & Beans", "RC")
Vahl = Human("Valentine", "Ezeanya", "Rice & Ofe Akwu", "Henieken")
Esther = Human("Esther", "Okoroafor", "Eba", "Malt")

print(Helen.drink())
print(Helen.eat())

print(Vahl.drink())
print(Vahl.eat())

print(Esther.drink())
print(Esther.eat())
print(Esther.lastname)

Scoobie = Dog("Bone", "Milk and Blood")
Max = Dog("Dog Food", "Serum")

print(Max.eat())
print(Max.drink())
print(Scoobie.eat())
print(Scoobie.drink())