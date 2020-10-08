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
    def __init__(self, name, weapon, lvl, subclass):
        super().__init__(name, weapon, lvl)
        self.subclass = subclass

x = SetX()
a1 = Fighter("Eveehi","Sword",3, "Defender")
a2 = Fighter("Aelien","Spear",3, "Weapon Master")
a1.skill = "Hammer"
print(a1.subclass)
a1.identfunc()
a2.identfunc()