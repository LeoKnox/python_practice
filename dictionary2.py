dictinay_test = {"name":"Flem", 1:"test"}
empty = {}

print(dictinay_test[1])
empty['fill'] = "not empty"
empty['more'] = "more empty"
empty['aone'] = "a new"

print(empty.pop('aone'))
print(empty)

print(empty.popitem())

empty.clear()
print(empty)

del(empty)
