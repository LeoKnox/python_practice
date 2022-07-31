def plusMinus(arr):
    neg = 0
    negl = 0
    pos = 0
    posl = 0
    zero = 0
    for i in arr:
        if i < 0:
            neg += abs(i)
            negl += 1
        elif i > 0:
            pos += i
            posl += 1
        else:
            zero += 1
    print (pos/len(arr))
    print (neg/len(arr))
    print (zero/len(arr))
