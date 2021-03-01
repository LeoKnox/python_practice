class Character(object):
    def __init__(self, name):
        self.name = name
    
    def getChar(self):
        return self.name
    
    def isActive(self):
        return False

class Active(Character):
    def isActive(self):
        return True

c1 = Character("Elric")
print(c1.getChar(), c1.isActive())

c1 = Active("Aelien")
print(c1.getChar(), c1.isActive())