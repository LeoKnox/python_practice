def caesarCipher(s, k):
    #a=97 z=122 A=65 Z=90
    #return(str(ord('a')) + " " + str(ord('z')))
    n = ""
    for i in s:
        if i.isalpha():
            n += chr(ord(i)+k)
        else:
            n += i
    return(n)
