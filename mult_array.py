import sys
from itertools import product

x = []
x.append(input().split(' '))
x.append(input().split(' '))
#print(list(product(*x)))
for p in list(product(*x)):
    print(p)
