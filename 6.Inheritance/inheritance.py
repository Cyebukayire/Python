class Dog():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(str(self.name) + " barks")


simba = Dog(234)
simba.talk()