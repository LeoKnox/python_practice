def lonelyinteger(a):
    d = {}
    for i in a:
        d[i] = d.get(i, 0)+1
    return d
