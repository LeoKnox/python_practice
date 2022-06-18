newset = {}
for i in range(int(input())):
    x = input()
    newset[x] = newset.get(x, 0) + 1
print(len(newset))
y = ""
for i in newset.values():
    y = y + str(i) + " "
print(y)
