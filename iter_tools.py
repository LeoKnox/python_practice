def recur_iter(a, b):
    if type(a) == list:
        for i in a:
            recur_iter(i, b)
    else:
        print(b, a)
        return(a)

a = input().split()
b = input().split()

#print(list(a))
#print(b)
ans = ""
recur_iter(a, 8)
