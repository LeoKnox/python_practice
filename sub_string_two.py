def count_substring(string, sub_string):
    print(len(string)-len(sub_string))
    for ch in string[0:len(string)-len(sub_string):1]:
        print(ch)
