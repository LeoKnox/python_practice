def repeatedString(s, n):
    runs = n//len(s)
    cnts = s.count('a')
    total = runs*cnts
    for i in range(n%len(s)):
        if s[i] == 'a':
            total+=1
    return (total)
