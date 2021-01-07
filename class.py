class Character(object):
    def __init__(self, char_name, char_class, level):
        self.char_name = char_name
        self.char_class = char_class
        self.level = level
        self.title = "The " + char_class + " called " + char_name + "!")
        
        def greet(self):
            print("My name is " + self.char_name + " and I am a " + self.char_class + "!")

a = Character("Aelien", "Fight", 3)
print(a.title)
a.greet()

'''
class MyClass:
    pass

my_inst = MyClass()
my_inst.__class__
print(issubclass(MyClass, object))
'''
