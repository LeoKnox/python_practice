def getMinimumCost(k, c):
    i = len(c)-1
    total = 0
    while i >= 0:
        for j in range(n):
            total += ((n-i//n)+1)*c[i-j]
        total += c[i]
        i -= n
    return total
