def getMinimumCost(k, c):
    i = len(c)-1
    total = 0
    m = 0
    alist = []
    while i >= 0:
        for j in range(k):
            total += (m+1)*c[i-j]
            if i - j == 0:
                return total
        i -= k
        m += 1
    return total
