def rotLeft(a, d):
    first = a[:d]
    second = a[d:]
    for f in first:
        second.append(f)
    return(second)
