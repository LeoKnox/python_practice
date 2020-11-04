import random

class MyChar:
    def __init__(self, name, atk, ac):
        self.name = name
        self.atk = atk
        self.ac = ac

def hit(off_atk, def_ac):
    roll = random.randint(1, 7) + off_atk
    if roll > def_ac:
        print("hit")
        print("Damage: " + str(random.randint(1,9)))
    else:
        print ("swish")
    print(roll)

c1 = MyChar("Elric", 12, 12)
c2 = MyChar("Yrkon", 11, 11)

print (c1.name)
print (c1.atk + c1.ac)
hit(c1.atk,c2.ac)
