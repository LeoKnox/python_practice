class Adventurer:
  def __init__(self, name, specilization, race):
    self.name = name
    self.specilization = specilization
    self.race = race
    self.level = 1

myadv = Adventurer("Elric", "fighter/mage", "elf")
print(myadv.level)
