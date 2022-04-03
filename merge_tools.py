    '''
    groups = [string[i:i+k] for i in range(0, len(string), k)]
    ans = []
    for g in groups:
        temp = ""
        for i in g:
            if i not in temp:
                temp += i
        ans.append(temp)
    for a in ans:
        print(a)
    '''
    for i in range(0,len(string),k):
        ans = ""
        for j in range(i,i+k,1):
            if string[j] not in ans:
                ans += string[j]
        print(ans)
