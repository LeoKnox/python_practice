import random

class Adventurer:
  def __init__(self, name, specilization, race):
    self.name = name
    self.specilization = specilization
    self.race = race
    self.level = 1

  def show_level(self):
    print(f"{self.name} you are level {self.level}.")

  def attack(self):
    attack_roll = random.randrange(1,21,1)
    print(f"{self.name} strikes to hit with a {attack_roll}")

myadv = Adventurer("Elric", "fighter/mage", "elf")
myadv.show_level()
myadv.attack()
