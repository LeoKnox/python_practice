import sys
from collections import Counter

our_in = [];
total = 0
for i in sys.stdin:
    our_in.append(i)
new_cnt = our_in.pop()
new_cnt = Counter(our_in.pop())
for j in our_in:
    nums = [int(n) for n in j.split()]
    print(nums)
print(total)
