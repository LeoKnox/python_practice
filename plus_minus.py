def plusMinus(arr):
    neg = 0
    pos = 0
    zero = 0
    for i in arr:
        if i < 0:
            neg += abs(i)
        elif i > 0:
            pos += i
        else:
            zero += 1
    print (pos/len(arr))
    print (neg/len(arr))
    print (zero/len(arr))
