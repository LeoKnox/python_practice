def getMinimumCost(k, c):
    i = len(c)-1
    total = 0
    while i >= 0:
        total += c[i]
        i -= 1
    return total
