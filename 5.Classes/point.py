class  Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
                

    def move(self):
        print("move")
    

    def draw(self):
        print("draw")
        return 23

point1 = Point(23,34)
point1.draw()