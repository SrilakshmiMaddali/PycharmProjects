#Constructor definition
"""
class Person():
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hi, I am {self.name}")

john=Person("johny")
john.talk()
print(john.name)
"""

class Mammal():
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("barking dog")


class Cat(Mammal):
    def meow(self):
        print("Meows")

dog1=Dog()
dog1.walk()
dog1.bark()

cat1=Cat()
cat1.walk()
cat1.meow()