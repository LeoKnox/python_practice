def timeConversion(s):
    s = list(s)
    if s[-2] == 'P':
        s[0] = int(s[0]) + 1
        s[1] = int(s[1]) + 2
    "".join(s)
    return(s[0:len(s)-2])
