import re

for i in range(int(input())):
    x = input()
    print(re.match(r'[+-]?\d*\.\d+$', x) != None)
