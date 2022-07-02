def divisibleSumPairs(n, k, ar):
    pairs = 0
    test = []
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if (ar[i] + ar[j])%k == 0:
                test.append([ar[i], ar[j]])
                pairs += 1
    return pairs
