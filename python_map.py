import random

def hit(ac):
  x = random.randint(1,20)
  print(x)
  return x >= ac

char_acs=[13,16,19,18]

to_hit = map(hit, char_acs)

print(list(to_hit))
