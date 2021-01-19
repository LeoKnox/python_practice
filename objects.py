a = "Eveehi"
b = "Fighter"
c = 5

class character:
    def __init__(self, char_name = "", char_class = "", level = 1):
        self.char_name = char_name
        self.char_class = char_class
        self.level = level

my_char = character("Evehi", "Fighter", 5)


print (type(a))
print (type(c))
print (type(my_char))
print (my_char.level)