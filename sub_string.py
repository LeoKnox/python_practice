def count_substring(string, sub_string):
    position = 0
    sub_index = 0
    for ind, ch in enumarate(string):
        if ch == sub_string[sub_index]:
            print(ind)
    return
