def diagonalDifference(arr):
  first = 0
  second = 0
  x = [0, 1,2]
  l = 2
  for i in x:
    first += arr[i][i]
    second += arr[l-i][i]
    #x.append([arr[i][len(arr)-i], arr[len(arr)-i][i]])
  return(abs(first-second))
