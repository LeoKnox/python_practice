class Adventurer:
  def __init__(self, name, specilization, race):
    self.name = name
    self.specilization = specilization
    self.race = race
    self.level = 1

  def show_level(self):
    print("You are level %s." %(self.level))

myadv = Adventurer("Elric", "fighter/mage", "elf")
myadv.show_level()
