class Char_Class:
    hp = 50

    def __init__(self, name): # constructor
        self.name = name
    
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