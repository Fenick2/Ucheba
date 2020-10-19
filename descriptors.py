class CoordValue:
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point:
    coordX = CoordValue()  # это дескрипторы
    coordY = CoordValue()

    def __init__(self, x, y):
        self.coordX = x
        self.coordY = y


pt1 = Point(1, 2)
pt2 = Point(3, 4)
