def maximumToys(prices, k):
    prices.sort()
    total = 0
    for i in prices:
        if not (total + i) > k:
            total += 1
    return(total)
