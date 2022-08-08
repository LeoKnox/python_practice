def diagonalDifference(arr):
  first = 0
  second = 0
  x = [0]
  for i in range(0,len(arr)):
    #first += arr[i][len(arr)-i]
    #second += arr[len(arr)-i][i]
    #x.append([arr[i][len(arr)-i], arr[len(arr)-i][i]])
    x[0] += 1
  #return(abs(first-second))
    return (len(arr))
