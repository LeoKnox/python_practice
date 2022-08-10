def superDigit(n, k):
    t = 0
    l = list(n)
    while (len(l) > 1):
        for i in l:
            t += int(i)
        l = list(str(t))
        t = 0
        k -= 1
    return(l)
