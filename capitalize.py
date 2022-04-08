def solve(s):
    for i, c in enumerate(s):
        if i == 0:
            s = s[:i] + s[i].upper() + s[i+1:]
        if s[i] == " ":
            s = s[:i+1] + s[i+1].upper() + s[i+2:]
    return(s)
