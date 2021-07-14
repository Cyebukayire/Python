
class Mammal():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(str(self.name) + " walks")

# class Dog(Mammal): #Inheritance
#     pass #Python doesn't like emmpty classes, so, this line will fill the gap

# simba = Dog("Simba")
# simba.walk()
    