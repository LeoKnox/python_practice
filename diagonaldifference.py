def diagonalDifference(arr):
  first = 0
  second = 0
  for i in range(0,len(arr)-1):
    for j in (0,len(arr)-1, -1):
      first += arr[i][j]
      second += arr[j][i]
  return("f",abs(first-second))
