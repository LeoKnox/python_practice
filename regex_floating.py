import re

for i in range(int(input())):
    x = input()
    print(re.search(r'\.[0-9]', x))
