def getMinimumCost(k, c):
    i = len(c)-1
    total = 0
    alist = []
    while i >= 0:
        for j in range(k):
            total += ((i//k)+1)*c[i-j]
            if (i - k) >= 0:
                total += ((i//k)+1)*c[i-j]
                alist.append(((i//k)+1)*c[i-j])
            else:
                total -= c[i-k]
        i -= k
    return total
