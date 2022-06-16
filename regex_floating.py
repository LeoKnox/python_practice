import re

for i in range(int(input())):
    x = input()
    print(re.search(r'[+-]?\d*\.\d+$', x) != None)
