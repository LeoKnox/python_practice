def maxMin(k, arr):
    arr.sort()
    fairness=arr[k]
    for i in range(len(arr)-k):
        if (arr[(i+k)-1])-(arr[i]) < fairness:
            fairness = arr[i+k-1]-arr[i]
    return(fairness)
