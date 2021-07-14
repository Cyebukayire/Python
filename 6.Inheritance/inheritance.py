class Dog():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("barks")


simba = Dog("Simba")
simba.talk()