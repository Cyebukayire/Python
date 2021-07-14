class Dog():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name + " barks")


simba = Dog("Simba")
simba.talk()