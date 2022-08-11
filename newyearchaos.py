def minimumBribes(q):
    n = []
    for i in range(len(q)):
        if q[i] > i+1:
            diff = q[i]-(i+1)
            if diff > 2:
                print('Too chaotic')
                return()
            print(":",i-q[i]+1)
            n.append(diff)
            #print(i, q[i], (q[i]-(i+1)))
        #else:
            #print(i, q[i], '0')
    print(sum(n))
