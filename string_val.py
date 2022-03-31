if __name__ == '__main__':
    s = input()
    ans = [False, False, False, False, False]
    for ch in s:
        if ch.isalnum():
            ans[0] = True
        if ch.isalpha():
            ans[1] = True
        if ch.isdigit():
            ans[2] = True
        if ch.islower():
            ans[3] = True
        if ch.isupper():
            ans[4] = True
    for a in ans:
        print(a)
