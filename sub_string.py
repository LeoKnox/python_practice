def count_substring(string, sub_string):
    position = 0
    sub_index = 0
    for i, ch in enumerate(string):
        if ch == sub_string[sub_index] and sub_index != len(sub_string)-1:
            if position == 0:
                position = i
            sub_index = sub_index + 1
        elif sub_index == len(sub_string)-1:
            return position
        elif sub_index > 0:
            sub_index = 0
            position = 0
    return "error"
