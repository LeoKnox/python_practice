def jumpingOnClouds(c):
    jumps = 0
    i = 0
    j = []
    #for i in range(len(c)-2):
    while i < len(c)-2:
        j.append([jumps, i])
        if c[i+2] != 1:
            i += 1
        jumps += 1
        i += 1
    
    return jumps
