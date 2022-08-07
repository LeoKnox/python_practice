def diagonalDifference(arr):
  first = 0
  second = 0
  for i in range(0,len(arr)):
    for j in (len(arr),0):
      first += arr[i][j]
      second += arr[j][i]
  return(abs(first-second))
