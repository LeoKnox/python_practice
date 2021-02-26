class CharClass:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
    
	def charDescription(self):
		print("Char name: " + self.name + " is " + self.lvl)

c1 = CharClass("Eveehi", 1)
c1.charDescription()
c1.lvl = c1.lvl + 1
c1.charDescription()
