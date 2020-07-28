from dataclasses import dataclass

@dataclass
class Armor:
    armor: float
    description: str
    level: int = 1
def power(self) -> float:
    return self.armor * self.level

armor = Armor(5.2, “Common armor.”, 2)
armor.power() # 10.4
print(armor)


# class Armor:
# def __init__(self, armor: float, description: str, level: int = 1):
#     self.armor = armor
#     self.level = level
#     self.description = description
# def power(self) -> float:
#     return self.armor * self.level

# armor = Armor(5.2, “Common armor.”, 2)
# armor.power() # 10.4
# print(armor)
