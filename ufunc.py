class SetX:
    x = 5

class Adventurer:
    def __init__(self, name, skill, lvl):
        self.name = name
        self.skill = skill
        self.lvl = lvl
    
    def identfunc(self):
        print("I am " + self.name + "and I use " + self.skill + "!")

x = SetX()
a1 = Adventurer("Eveehi","Sword",3)
a2 = Adventurer("Aelien","Spear",3)
a1.identfunc()
a2.identfunc()