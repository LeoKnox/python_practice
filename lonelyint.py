def lonelyinteger(a):
    d = {}
    for i in a:
        if d[a] == None:
            d[a] = 1
        else:
            d[a] += 1
    return d
