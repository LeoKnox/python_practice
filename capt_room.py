from collections import Counter

k = int(input())
rooms = Counter(input())
for r in rooms:
    if (r[0] != ' ' and rooms[r[0]] !=k):
        print(r[0])
