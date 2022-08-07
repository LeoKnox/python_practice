def diagonalDifference(arr):
    for i in range(0,len(arr)):
        for j in (len(arr), 0, -1):
          print('i', i, 'j', j)
    return("f",len(arr))


arr = [[1,2,3], [4,5,6]]
diagonalDifference(arr)
