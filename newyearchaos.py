def minimumBribes(q):
    bribes = {}
    for i in range(len(q)):
        if i != q[i]:
            bribes[i] = q[i]
    print (bribes, "D")
