def luckBalance(k, contests):
    contests.sort()
    total = 0
    for c in contests[::-1]:
        if k > 0 and c[1] > 0:
            total += c[0]
            k -= 1
        elif k <= 0 and c[1] != 0:
            total -= c[0]
        else:
            total += c[0]
    return(total)
