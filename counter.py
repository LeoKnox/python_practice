import sys
from collections import Counter

our_in = [];
for i in sys.stdin:
    our_in.append(i);
print(Counter(our_in[1]))
