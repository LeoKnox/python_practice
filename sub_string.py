    position = 0
    sub_index = 0
    for i, ch in enumerate(string):
        if ch == sub_string[sub_index]:
            position = position + 1
            print(i)
        elif position > 0:
            position = 0
    return
