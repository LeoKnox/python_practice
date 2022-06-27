def minimumAbsoluteDifference(arr):
    total = abs(arr[0] - arr[1])
    index = 0
    while index < len(arr):
        temp = index + 1
        while temp < len(arr):
            if abs(arr[index]-arr[temp]) < total:
                total = abs(arr[index]-arr[temp])
            temp += 1
        index += 1
    return total
