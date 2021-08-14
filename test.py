x = "word"
y = "xwords"
b = False

for i in x:
    for j in y:
        if j==i:
            b = True
            print(i)
        elif j!=1:
            b = False

if b:
    print('yes')