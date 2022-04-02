def merge_the_tools(string, k):
    groups = [string[i:i+k] for i in range(0, len(string), k)]
    ans = []
    for g in groups:
        temp = ""
        for i in g:
            if i not in temp:
                temp += i
        ans.append(temp)
    print(ans)
