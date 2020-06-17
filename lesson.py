class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, z):
        return ((self.x - z.x) ** 2 + (self.y - z.y) ** 2) ** 0.5


p1 = Point(12.7, 1)
p2 = Point(1.5, 2)
print(p1.dist(p2))
