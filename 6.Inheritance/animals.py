from inheritance import Mammal

class Dog(Mammal): #inheritance
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(str(self.name) + " barks")


class Cat(Mammal): #inheritance
    pass #Python doesn't like emmpty classes, so, this line will fill the gap