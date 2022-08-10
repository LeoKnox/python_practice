def superDigit(n, k):
    t = 0
    l = list(n)
    while (len(l) > 1):
        for i in l:
            t += int(i)
        l = list(str(t))
        t = 0
    #return(k*int(l[0]))
    return(l[0]*k)
