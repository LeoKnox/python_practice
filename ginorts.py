oldstring = input()
charDict = {}

for i in oldstring:
    if i.isupper():
        charDict['upper'] = charDict.get('upper', '') + i
    if i.islower():
        charDict['lower'] = charDict.get('lower', '') + i
    if i.isnumeric() and int(i)%2 == 0:
        charDict['even'] = charDict.get('even', '') + i
    if i.isnumeric() and int(i)%2 == 1:
        charDict['odd'] = charDict.get('odd', '') + i
print(''.join(charDict['lower'])+''.join(charDict['upper'])+''.join(charDict['odd'])+''.join(charDict['even']))
