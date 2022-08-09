def caesarCipher(s, k):
    #a=97 z=122
    #return(str(ord('a')) + " " + str(ord('z')))
    n = ""
    for i in s:
        if (ord(i) > 97) and (ord(i) < 122):
            n += chr(ord(i)+k)
        else:
            n += i
    return(n)
