def luckBalance(k, contests):
    contests.sort()
    total = 0
    for c in contests[::-1]:
        if c[1] != 1:
            k = k - 1
            total += c[0]
    return(total)
