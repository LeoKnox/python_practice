def minimumBribes(q):
    for i in range(len(q)):
        if q[i] > i+1:
            print(i, q[i], (q[i]-(i+1)))
        else:
            print(i, q[i], '0')
    print('a')
