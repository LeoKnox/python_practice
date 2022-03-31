def merge_the_tools(string, k):
    groups = [string[i:i+k] for i in range(0, len(string), k)]
    for g in groups:
        ans = str(set(g))
        print(ans)
    print(groups)
