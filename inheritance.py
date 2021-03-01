class Character(object):
    def __init__(self, name):
        self.name = name
    
    def getChar(self):
        return self.name
    
class Fighter(Character):
    def __init__(self, name, subclass):
        super().__init__(name)
        self.subclass = subclass

    def showClass(self):
        print("Character is", self.name, "and is a", self.subclass, "Fighter")

x = Fighter("Aelien", "Swordsman")
y = Fighter("Eveehi", "Archer")
y.showClass()
x.showClass()