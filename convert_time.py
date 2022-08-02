def timeConversion(s):
    s = list(s)
    if s[-2] == 'P':
        s[0] = str(int(s[0]) + 1)
        s[1] = str(int(s[1]) + 2)
    s = list(s)
    "".join(s)
    return(s[0:len(s)-2])
