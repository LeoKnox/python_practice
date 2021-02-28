class Empty:
    pass

class Char_Class:
    __hp = 50

    def __init__(self, name): # constructor
        self.name = name
    
    def takeDamage(self, damage):
        self.__hp -= damage
    
    def char_method(self):
        print('Hail, I am adventurer', self.name)
    
    def addArmor(self, armor):
        self.armor = armor
    
    def displayarmor(self):
        return self.armor

obj = Char_Class("Elric")
obj.char_method()
print(obj.hp)
obj.addArmor("Plate")
print("Wearing armor", obj.displayarmor())
obj.takeDamage(3)
