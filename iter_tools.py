def recur_iter(a):
    if type(a) == list:
        for i in a:
            recur_iter(i)
    else:
        print(a)
        return(a)

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
