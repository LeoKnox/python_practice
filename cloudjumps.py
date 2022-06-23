def jumpingOnClouds(c):
    jumps = 0
    i = 0
    j = []
    while i < len(c)-2:
        if c[i+2] != 1:
            i += 1
        jumps += 1
        i += 1
        j.append([jumps, i])    
    return j
