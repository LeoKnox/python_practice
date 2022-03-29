def count_substring(string, sub_string):
    #print(len(string)-len(sub_string))
    total = 0
    for i, ch in enumerate(string[0:len(string)-len(sub_string)+1:1]):
        if sub_string == string[i:i+len(sub_string)]:
            total += 1
            #print("yeah")
        #print(string[i:i+len(sub_string)])
    return total
