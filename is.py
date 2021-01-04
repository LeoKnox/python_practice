a = "I am true"
b = "I am true"

a == b #True
a is b #False

a = [1,2,3,4]
b = a
a == b  #True
a is b  #True

b = a[:]
a == b  #True
a is b  #False
