def minimumBribes(q):
    bribes = {}
    total = 0
    for i in range(len(q)):
        if i != q[i]:
            total += (q[i] - (i+1))
            bribes[i+1] = q[i]
    print (total)
