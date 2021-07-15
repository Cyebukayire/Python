
class Mammal(): #Inherited by Dog & Cat in animals module
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(str(self.name) + " walks")

"""
DOG OBJECT 
"""
# class Dog(Mammal): #Inheritance
#     pass #Python doesn't like emmpty classes, so, this line will fill the gap


"""
CAT OBJECT 
"""
# class Cat(Mammal):
#     def __init__(self, name):
#         self.name = name
#     def be_annoying(self):
#         print(str(self.name) + " is annoying!")


"""
IMPLEMENTATION OF OBJECTS IN THE SAME CLASS AS PARENT CLASS 
"""
# simba = Dog("Simba")
# simba.walk()
    
# cat = Cat("my cat")
# cat.walk()
# cat.be_annoying()

