def miniMaxSum(arr):
    arrz = arr.sort()
    sum = 0
    for i in arrz:
        sum += i
    print(sum-arrz[len(arrz)-1], sum-arrz[0])
