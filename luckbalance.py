def luckBalance(k, contests):
    contests.sort()
    total = 0
    for c in contests[::-1]:
        if k > 0:
            total += c[1]
        if c[1] == 1:
            k = k - 1
    return(total)
