def lonelyinteger(a):
    d = {}
    for i in a:
        d[i] = d.get(i, 0)+1
    for key in d.keys():
      print('a', key)
      if d[key] > 1:
        print (d[key])
    return ('x')
