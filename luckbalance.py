def luckBalance(k, contests):
    contests.sort()
    total = 0
    for c in contests[::-1]:
        if k > 0:
            total += c[0]
        if k == 0 and c[1] != 0:
            total -= c[0]
        if c[1] == 1:
            k = k - c[1]
    return(total)
