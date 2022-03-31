def merge_the_tools(string, k):
    groups = [string[i:i+k] for i in range(0, len(string), k)]
    print(groups)
