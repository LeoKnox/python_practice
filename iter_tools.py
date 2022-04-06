a = input()
b = input()

#print(a)
#print(b)
ans = ""
for i in a[0:3:2]:
    for j in b[0:3:2]:
        ans += "("+i+", "+j+")"+" "
print(ans)
