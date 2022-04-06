a = input()
b = input()

#print(a)
#print(b)
ans = ""
for i in a[0:len(a):2]:
    for j in b[0:len(b):2]:
        ans += "("+i+", "+j+")"+" "
print(ans)
