# -*- coding: utf-8 -*-
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.life_time = 3

    def move(self, x, y):
        pass

    def interact(self, other):
        pass

    def logic(self):
        return self.life_time - 1


class Bomb(GameObject):
    def life_time(self):
        if self.life_time == 0:
            self.alive is False
        



b = Bomb(3,4)
print(b.x, b.y, b.alive)
print(b.life_time)

b.logic()
print(b.life_time == 2)
b.logic()
print(b.life_time == 1, b.alive)
b.logic()
print(b.life_time == 0, not b.alive) 
