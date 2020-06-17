class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def move(self, x, y):
        pass

    def interact(self, other):
        pass

    def logic(self):
        pass


class Bomb(GameObject):
    def __init__(self, x, y, life_time=3):
        GameObject.__init__(self, x, y)
        self.life_time = life_time

    def logic(self):
        self.life_time -= 1
        if self.life_time == 0:
            self.alive = False




b = Bomb(3, 4)
print(b.x == 3)
print(b.y == 4)
print(b.alive)

b.logic()
print(b.life_time == 2)
b.logic()
print(b.life_time == 1)
print(b.alive)
b.logic()
print(b.life_time == 0)
print(not b.alive)