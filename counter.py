import sys
from collections import Counter

def price_shoe(order):
    o = order.split(" ")
    return o
    
our_in = [];
for i in sys.stdin:
    our_in.append(i)
new_cnt = our_in.pop()
new_cnt = Counter(our_in.pop())
total = map(price_shoe, our_in)
print(total)
