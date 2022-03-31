def merge_the_tools(string, k):
    groups = [string[i:i+k] for i in range(0, len(string), k)]
    for g in groups:
        ans = ''.join(set(g))
        print(ans)
    print(groups)
