def jumpingOnClouds(c):
    jumps = 0
    j = []
    for i in range(len(c)-2):
        j.append([jumps, i])
        if c[i+2] != 1:
            i += 1
        jumps += 1
    
    return j
