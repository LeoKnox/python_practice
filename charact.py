import random

class Adventurer:
  def __init__(self, name, specilization, race):
    self.name = name
    self.specilization = specilization
    self.race = race
    self.level = 1

  def show_level(self):
    print(f"{self.name} you are level {self.level}.")

  def show_exp(self):
    xp = 27.833
    print(f"This much {xp:.2f}")

  def attack(self):
    loc=["low", "middle", "high"]
    wt=[3, 7, 2]
    attack_location = random.choices(loc, wt)
    attack_roll = random.randrange(1,21,1)
    print(f"{self.name} strikes to hit with a {attack_roll} at {attack_location}{' critical!' if attack_roll == 20 else ''}")

  def add_weapons(self, *weapons):
    for weapon in weapons:
      print(f"adding {weapon} to inventory")

myadv = Adventurer("Elric", "fighter/mage", "elf")
myadv.show_level()
myadv.attack()
myadv.show_exp()

weapons = ['sword', 'staff', 'spear']
myadv.add_weapons('sword', 'staff', 'spear')
del weapons[1]
weapons.append('bow')
for x in weapons:
  if x == 'spear':
    print(f"{x} break")
    break
  else:
    print(x)
print(weapons.pop(0))
weapons.remove('bow')
print(weapons)
