def superDigit(n, k):
    t = 0
    l = list(n)
    while (len(n) > 1):
        for i in l:
            t += int(i)
        l = list(t)
        t = 0    
    return(t)
