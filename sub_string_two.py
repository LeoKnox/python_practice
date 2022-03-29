def count_substring(string, sub_string):
    print(len(string)-len(sub_string))
    for i, ch in enumerate(string[0:len(string)-len(sub_string):1]):
        print(string[i:i+3])
