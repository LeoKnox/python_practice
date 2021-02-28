class Char_Class:
    hp = 50

    def __init__(self, name): # constructor
        self.name = name
    
    def char_method(self):
        print('Hail, I am adventurer', self.name)

obj = Char_Class("Elric")
obj.char_method()
print(obj.hp)