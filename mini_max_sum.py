def miniMaxSum(arr):
    arr.sort()
    sum = 0
    for i in arr:
        sum += i
    print(sum-arr[len(arr)-1], sum-arr[0])
