class SetX:
    x = 5

class Adventurer:
    def __init__(self, name, skill, lvl):
        self.name = name
        self.skill = skill
        self.lvl = lvl

x = SetX()
a1 = Adventurer("Eveehi","Sword",3)
a2 = Adventurer("Aelien","Spear",3)
print(a1.name)
print(a2.name + " " + a2.skill)