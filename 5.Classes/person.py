class Person():
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("Hi! I am "+ self.name)
        return None


Person1 = Person("Hanson")
Person1.talk()

Kellia = Person("Kellia")
Kellia.talk()