def getMinimumCost(k, c):
    i = len(c)-1
    total = 0
    alist = []
    while i >= 0:
        for j in range(k):
            total += ((i//k)+1)*c[i-j]
            if (i - j) <= 0:
                return total
        i -= k
    return total
