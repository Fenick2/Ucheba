class Rectangle:
    def __init__(self, width, height, sign):
        self.w = width
        self.h = height
        self.s = sign

    def __str__(self):
        rect = []
        for i in range(self.h):
            rect.append(self.s * self.w)
        rect = '\n'.join(rect)
        return rect

    def __add__(self, c):
        return Rectangle(self.w + c.w, self.h + c.h, self.s )


a = Rectangle(8, 4, '*')
print(a)
b = Rectangle(5, 2, '#')
print(b)
print()
print(a+b)