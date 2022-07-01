def maxMin(k, arr):
    fairness=arr[1]
    for i in range(len(arr)-k):
        if (arr[i+k])-(arr[i]) < fairness:
            fairness = arr[i+k]-arr[i]
    return(fairness)
