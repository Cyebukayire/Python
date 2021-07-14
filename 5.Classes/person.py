class Person():
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("Hi! I am "+ str(self.name))
        return None


Person1 = Person("Hanson")
Person1.talk()