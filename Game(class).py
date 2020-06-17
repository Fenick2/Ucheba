class GameObject:
    def __init__(self, x, y, game):
        self.y = y
        self.x = x
        self.game = game
        self.alive = True
        self.passable = True
        self.interactable = True

    def interact(self, object):
        pass

    def process(self):
        pass

    def render(self):
        raise NotImplementedError


class Coin(GameObject):
    def render(self):
        return "$"


class Wall(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.game = game
        self.passable = False
        self.interactable = False

    def render(self):
        return "#"


class HeatWave(GameObject):
    def render(self):
        return "+"

    def process(self):
        self.alive = False
 
    def interact(self, object):
        if isinstance(object, (Player, SoftWall)):
            object.alive = False


class SoftWall(GameObject):
    def __init__(self, *args):
        super().__init__(*args)
        self.passable = False

    def render(self):
        return "%"

