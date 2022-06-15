import sys
from itertools import product

x = []
x.append(map(int, input().split()))
x.append(map(int, input().split()))
print(' '.join([str(y) for y in (list(product(*x)))]))
