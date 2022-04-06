a = input()
#b = input()

print(a)
#print(b)
ans = ""
a = list(a)
for i in a[0:len(a):1]:
    for j in i[0:len(i):1]:
        print(i, j)
        ans += "("+i+", "+j+")"+" "
print(ans)
