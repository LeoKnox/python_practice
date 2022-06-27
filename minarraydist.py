def minimumAbsoluteDifference(arr):
    arr.sort()
    total = abs(arr[0]-arr[1])
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < total:
            total = abs(arr[i] - arr[i+1])
    return total
