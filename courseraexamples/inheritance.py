class Fruit:
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor


class Apple(Fruit):
    pass

class Grape(Fruit):
    pass


granysmith=Apple("red","tart")
print(granysmith.color)



class Animal:
    sound=""
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name,sound=self.sound))

class Piglet(Animal):
    sound="Oink!"

class Cow(Animal):
    sound="Mooooo!"


hamlet=Piglet("Hamlet")
hamlet.speak()

milky=Cow("Milky")
milky.speak()

