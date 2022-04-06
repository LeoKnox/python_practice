def recur_iter(a):
    if type(a) == list:
        recur_iter(a)
    else:
        print(a)

a = input().split()
b = input().split()

#print(list(a))
#print(b)
ans = ""
recur_iter(a)
'''
for i in a[0:len(a):1]:
    for j in b[0:len(b):1]:
        #print(i, j)
        ans += "("+i+", "+j+")"+" "
print(ans)
'''
