# Магические методы сравнения
# __eq__ resolve == (equal)
# __ne__ resolve != (not equal)
# __lt__  --//-- <  (less than)
# __le__  --//-- <= (less or equal)
# __gt__  --//--  > (greater than)
# __ge__  --//-- >= (greater or equal)


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other
