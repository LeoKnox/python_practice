def jumpingOnClouds(c):
    jumps = 0
    j = []
    for i in range(len(c)-2):
        if c[i+2] != 1:
            i += 1
        jumps += 1
        j.append([i, jumps])
    
    return j
