def solve(s):
    print("***", type(s))
    for i, c in enumerate(s):
        if i == 0:
            print(s[i].upper())
            s = s[:i] + s[i].upper() + s[i+1:]
    return(s)
