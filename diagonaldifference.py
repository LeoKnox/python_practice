def diagonalDifference(arr):
  first = 0
  second = 0
  x = []
  for i in range(0,len(arr)):
    first += arr[i][len(arr)-i-1]
    second += arr[len(arr)-i-1][i]
    x.append([arr[i][len(arr)-i-1], arr[len(arr)-i-1][i]])
  #return(abs(first-second))
    return (x)
