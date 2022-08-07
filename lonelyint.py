def lonelyinteger(a):
    d = {}
    for i in a:
        d[i] = d.get(i, 0)+1
    for i in range(0,len(d)):
        print(i)
    return ('x')
