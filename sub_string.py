def count_substring(string, sub_string):
    position = 0
    sub_index = 0
    for i, ch in enumerate(string):
        if ch == sub_string[sub_index]:
            sub_index = sub_index + 1
            print(i)
        elif sub_index > 0:
            sub_index = 0
    return position
