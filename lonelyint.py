def lonelyinteger(a):
    d = {}
    for i in a:
        if not d[i]:
            d[i] = 1
        else:
            d[i] += 1
    return d
