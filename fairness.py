def maxMin(k, arr):
    arr.sort()
    fairness=arr[k]
    store = [arr]
    for i in range(len(arr)-k-1):
        if (arr[i+k-1])-(arr[i]) < fairness:
            store.append([arr[i+k], arr[i]])
            fairness = arr[i+k]-arr[i]
    return(store)
