def lonelyinteger(a):
    d = {}
    for i in a:
        d[i] = d.get(i, 0)+1
    for key in d:
        if d[key] > 1:
            return d[key]
    return ('x')
