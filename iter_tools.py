def recur_iter(a, b):
    if type(a) == list:
        for i in a[0]:
            print('a', i)
            recur_iter(i, b)
    else:
        print(b, a)
        return(a)

a = input().split()
b = input().split()

#print(list(a))
#print(b)
ans = ""
print(type(a))
if (type(a) == list):
    print('stet')
recur_iter(a, 8)
'''
for i in a[0:len(a):1]:
    for j in b[0:len(b):1]:
        #print(i, j)
        ans += "("+i+", "+j+")"+" "
print(ans)
'''
