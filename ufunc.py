class SetX:
    x = 5

class Adventurer:
    def __init__(self, name, weapon, lvl):
        self.name = name
        self.weapon= weapon
        self.lvl = lvl
    
    def identfunc(self):
        print("I am " + self.name + " and I use " + self.weapon + "!")

class Fighter(Adventurer):
    pass

x = SetX()
a1 = Fighter("Eveehi","Sword",3)
a2 = Fighter("Aelien","Spear",3)
a1.skill = "Hammer"
a1.identfunc()
a2.identfunc()