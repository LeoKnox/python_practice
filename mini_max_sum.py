def miniMaxSum(arr):
    sum = 0
    for i in arr:
        sum += i
    for j in arr:
        print(sum-j)
