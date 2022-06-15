import sys
from itertools import product

x = []
x.append(input().split())
x.append(input().split())
print(' '.join([str(y) for y in (list(product(*x)))]))
