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
    loc=["low", "middle", "high"]
    wt=[3, 5, 2]
    attack_location = random.choice(loc, wt)
    attack_roll = random.randrange(1,21,1)
    print(f"{self.name} strikes to hit with a {attack_roll} at {attack_location}")

myadv = Adventurer("Elric", "fighter/mage", "elf")
myadv.show_level()
myadv.attack()
