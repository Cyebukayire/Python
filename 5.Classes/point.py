class  Point:
    # We need constructors to initialize more objects
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
                

    def move(self):
        print("move")
    

    def draw(self):
        print("draw")
        return 23

point1 = Point(23,34, 44)
point1.draw()
print(point1.z)