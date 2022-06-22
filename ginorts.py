oldstring = input()
charDict = {}

for i in oldstring:
    if i.isupper():
        charDict['upper'] = charDict.get('upper', '') + i
    if i.islower():
        charDict['lower'] = charDict.get('lower', '') + i
print(charDict)
