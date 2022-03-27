def count_substring(string, sub_string):
    position = 0
    sub_index = 0
    print(sub_string[sub_index])
    for i, ch in enumerate(string):
        if ch == sub_string[sub_index]:
            sub_index = sub_index + 1
            print(sub_string)
        elif sub_index > 0:
            sub_index = 0
    return position
