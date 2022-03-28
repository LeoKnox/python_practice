def count_substring(string, sub_string):
    position = 0
    sub_index = 0
    print(sub_string[sub_index])
    for i, ch in enumerate(string):
        print(len(sub_string)-1, "***")
        if ch == (sub_string[sub_index] and sub_index == len(sub_string-1)):
            sub_index = sub_index + 1
            print(sub_string)
        elif sub_index > 0:
            sub_index = 0
        elif sub_index == len(sub_string)-1:
            return position
    return position
