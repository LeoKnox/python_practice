def divisibleSumPairs(n, k, ar):
    pairs = 0
    test = []
    for i in range(len(ar)):
        for j in range(i,len(ar)):
            if (ar[i] + ar[j])//k == 0:
                pairs += 1
    return pairs
