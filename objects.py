a = "Eveehi"
b = "Fighter"
c = 5

class character:
    def __init__(self, char_name = "", char_class = "", level = 1):
        self.char_name = char_name
        self.char_class = char_class
        self.level = level

my_char = character("Eveehi", "Fighter", 5)
two_char = character("Aelien", "mage", 4)
setattr(my_char,'char_race','Orc')
setattr(my_char,'defense', 15)

print (type(a))
print (type(c))
print (type(my_char))
print (my_char.level)
print (my_char.char_race)
print (getattr(my_char, 'defense', 'No defense!'))
print(getattr(my_char,'attack','No attack!'))
print (getattr(two_char, 'defense', 'No defense!'))
print(getattr(two_char,'attack','No attack!'))
