def jumpingOnClouds(c):
    jumps = 0
    for i in range(len(c)-2):
        jumps += 1
        if c[i+2] != 1:
            i += 1
    return jumps
