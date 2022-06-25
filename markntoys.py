def maximumToys(prices, k):
    prices.sort()
    ticket = 0
    total = 0
    for i in prices:
        if not (ticket + i) > k:
            total += 1
            ticket += i
    return(total)
