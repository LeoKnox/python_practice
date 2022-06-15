import sys
from itertools import product

x = []
y = []
x.append(input().split(' '))
y.append(input().split(' '))
print(list(product(x*y)))
