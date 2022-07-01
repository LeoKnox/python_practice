def getMinimumCost(k, c):
    i = len(c)-1
    total = 0
    m = 0
    alist = []
    while i >= 0:
        for j in range(k):
            total += (m+1)*c[i-j]
        i -= k
        m = 1
    return total
