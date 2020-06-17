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


b = Rectangle(8, 4, '*')
print(b)
