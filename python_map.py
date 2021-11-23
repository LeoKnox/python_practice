def hit(ac):
  return 18 > ac

char_acs=[13,16,19,18]

to_hit = map(hit, char_acs)

print(list(to_hit))
