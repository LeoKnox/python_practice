def getMinimumCost(k, c):
    i = len(c)-1
    total = 0
    alist = []
    while i >= 0:
        for j in range(n):
            total += ((i//k)+1)*c[i-j]
            alist.append((n-i)*c[i-j])
            alist.append(i//k)
        i -= k
    return total
