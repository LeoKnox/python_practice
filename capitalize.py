def solve(s):
    print("***", type(s))
    for i, c in enumerate(s):
        if i == 0:
            print(s[i].upper())
            s = s[i].upper() + str[i+1:]
    return(s)
