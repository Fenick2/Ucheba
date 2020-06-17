class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def dist(self, z):
        return ((self.x - z.x) ** 2 + (self.y - z.y) ** 2) ** 0.5


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def square(self):
        return (3.14 * self.radius ** 2)

    def do_intersect(self, a):
        return (self.center).dist(a.center) < (a.radius + self.radius)

    def __repr__(self):
        return f'Circle({self.center}, {self.radius})'

    def __lt__(self, other):
        return self.square() < other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __eq__(self, other):
        return self.square() == other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __ne__(self, other):
        return self.square() != other.square()
