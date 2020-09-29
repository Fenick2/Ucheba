# Вычисляемые property
class Rectangle:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        self.__area = None

    @property
    def side_a(self):
        return self.__a

    @side_a.setter
    def side_a(self, value):
        self.__a = value
        self.__area = None

    @property
    def side_b(self):
        return self.__b

    @side_b.setter
    def side_b(self, value):
        self.__b = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.side_a * self.side_b
        return self.__area
