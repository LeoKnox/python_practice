def divisibleSumPairs(n, k, ar):
    pairs = 0
    test = []
    for i in range(len(ar)):
        for j in range(i,len(ar)):
            test.append([i,j])
    return test
