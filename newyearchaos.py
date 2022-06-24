def minimumBribes(q):
    bribes = {}
    for i in range(len(q)):
        if i != q[i]:
            bribes[i+1] = q[i]
    print (bribes)
