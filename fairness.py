def maxMin(k, arr):
    arr.sort()
    fairness=arr[k]
    store = []
    for i in range(len(arr)-k):
        if (arr[i+k])-(arr[i]) < fairness:
            for j in range(k-1):
                store.append(arr[i+j])
            fairness = arr[i+k]-arr[i]
    return(k)
