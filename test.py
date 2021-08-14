x = "word"
y = "wordx"
b = True
first = True
second = False
third = False
i = 0

for i in range(len(y)):
    for j in range(len(x)):
        if y[i]==x[j]:
            print(x[j])
        else:
            first = False

if b:
    print('first')