def caesarCipher(s, k):
    n = ""
    k = k % 26
    for i in s:
        if i.isalpha():
            if (i.islower()) and (ord(i)+k > 122):
                n += chr(ord(i)+k-26)
            elif (i.isupper()) and (ord(i) + k > 90):
                n += chr(ord(i)+k-26)
            else:
                n += chr(ord(i)+k)
        else:
            n += i
    return(n)
