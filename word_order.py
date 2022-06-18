newset = {}
for i in range(int(input())):
    x = input()
    newset[x] = newset.get(x, 0) + 1
print(len(newset))
print(newset, sep=' ')
