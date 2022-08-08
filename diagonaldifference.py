def diagonalDifference(arr):
  first = 0
  second = 0
  x = []
  for i in range(0,len(arr)-1):
    first += arr[i][len(arr)-i]
    second += arr[len(arr)-i][i]
    x.append([arr[i][len(arr)-i], arr[len(arr)-i][i]])
  #return(abs(first-second))
    return (x)
