def diagonalDifference(arr):
  first = 0
  second = 0
  for i in range(0,len(arr)):
    first += arr[i][i]
    second += arr[len(arr)-i-1][i]
  return(abs(first-second))
