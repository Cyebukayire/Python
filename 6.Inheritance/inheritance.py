class Mammal():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(str(self.name) + " walks")

class Dog(Mammal): #Inheritance
    pass #Python doesn't like emmpty classes, so, this line will fill the gap


class Cat(Mammal):
    pass


simba = Dog("Simba")
simba.walk()
    
cat = Cat("a cat")
cat.walk()