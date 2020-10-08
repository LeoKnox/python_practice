class SetX:
    x = 5

class Adventurer:
    def __init__(self, name, weapon, lvl):
        self.name = name
        self.weapon= weapon
        self.lvl = lvl
    
    def identfunc(self):
        print("I am " + self.name + " and I use " + self.weapon + "!")

class Scout(Adventurer):
    def __init__(self, name, weapon, lvl, specialty):
        super().__init__(name, weapon, lvl)
        self.specialty = specialty
    
    def subclassattack(self):
        print(f"{self.name} attack with {self.specialty} and {self.weapon}")

class Fighter(Adventurer):
    def __init__(self, name, weapon, lvl, subclass):
        super().__init__(name, weapon, lvl)
        self.subclass = subclass
    
    def subclassattack(self):
        print(f"{self.name} attack uses {self.subclass} with {self.weapon}")

x = SetX()
a1 = Scout("Eveehi","Sword",3, "Sniper")
a2 = Fighter("Aelien","Spear",3, "Weapon Master")
a1.skill = "Hammer"
print(a1.weapon)
a1.identfunc()
a1.subclassattack()
a2.subclassattack()